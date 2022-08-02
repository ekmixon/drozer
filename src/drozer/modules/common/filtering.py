class Filters(object):
    """
    Utility methods for filtering collections of ReflectedTypes.
    """

    def match_filter(self, collection, key, term):
        """
        Implements a filter for items in collection, where the value of the
        property 'key' is equal to 'term'.
        """

        if collection is None:
            collection = []

        if term not in [None, ""]:
            return filter(
                lambda e: str(term).upper() in str(getattr(e, key)).upper(),
                collection,
            )

        else:
            return collection
