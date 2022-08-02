import os, tempfile
from mwr.common import fs

from drozer.modules.common import file_system

class SuperUser(file_system.FileSystem):
    """
    Utility methods for aiding with superuser binary detection and installation
    of "minimal su" on the Agent.
    """

    def suPath(self):
        """
        Get the path to which su is uploaded on the Agent.
        """

        return f"{self.workingDir()}/su"

    def _localPathMinimalSu(self):
        """
        Get the path to the su binary on the local system.
        """

        return os.path.join(os.path.dirname(__file__) , "..", "tools", "setup", "minimal-su", "libs", "armeabi", "su")

    def __agentPathScript(self):
        """
        Get the path to which the install script is uploaded on the Agent.
        """

        return f"{self.workingDir()}/install-minimal-su.sh"

    def isAnySuInstalled(self):
        """
        Test whether any su binary is installed on the Agent.
        """
        
        return (self.exists("/system/bin/su") or self.exists("/system/xbin/su"))
            
    def isMinimalSuInstalled(self):
        """
        
        Test whether the 'minimal su' binary is installed on the Agent.
        """
        
        return (self.md5sum("/system/bin/su") == fs.md5sum(self._localPathMinimalSu()))

    def suExec(self, command):
        """
        Execute a command as root, using minimal-su
        """

        self.shellExec("su -c \"" + command + "\"")

    def uploadMinimalSu(self):
        """
        Upload minimal su to the Agent.
        """

        # Remove existing uploads of su
        self.shellExec(f"rm {self.workingDir()}/su")

        bytes_copied = self.uploadFile(self._localPathMinimalSu(), self.suPath())

        return bytes_copied == os.path.getsize(self._localPathMinimalSu())

    def uploadMinimalSuInstallScript(self):
        """
        Upload minimal su install script to the Agent.
        """

        # Remove existing uploads of su install script
        self.shellExec(f"rm {self.workingDir()}/install-minimal-su.sh")

        minimal_su_script = """#!/system/bin/sh

mount -o remount,rw /system
cat $REPLACEME$/su > /system/bin/su
chmod 4755 /system/bin/su
echo 'Done. You can now use `su` from a drozer shell.'
"""

        minimal_su_script = minimal_su_script.replace("$REPLACEME$", self.workingDir())

        tempDir = tempfile.mkdtemp()
        localPathScript = os.path.join(tempDir, "install-su.sh")
        fs.write(localPathScript, minimal_su_script)

        bytes_copied = self.uploadFile(localPathScript, self.__agentPathScript())

        if bytes_copied != os.path.getsize(localPathScript):
            return False
        self.shellExec(f"chmod 770 {self.__agentPathScript()}")
        return True

