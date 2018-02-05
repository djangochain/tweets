from django.db.models import Q
import operator

class QueryBuilder(object):
    def __init__(self, data):
        self.criteria = data["criteria"]

    __equals__ = "equals"
    __contains__ = "contains"
    __startswith__ = "startswith"
    __endswith__ = "endswith"
    __gt__ = "gt"
    __gte__ = "gte"
    __lt__ = "lt"
    __lte__ = "lte"
    __regex__ = "regex"
    __range__ = "range"

    def _get_fragments(self):
        bool_query_fragments = {
            "AND": [],  # must
            "OR": [],  # should
            "NOT": []  # must_not
        }
        for operator_type,criteria in self.criteria.items():
            for operator_criteria in criteria:
                query_type_obj = self._get_filter_query_pattern(operator_criteria)
                if query_type_obj:
                    bool_query_fragments[operator_type].append(query_type_obj)

        return bool_query_fragments

    def _get_filter_query_pattern(self,operator_criteria):
        operator = operator_criteria["operator"]
        field = operator_criteria["fields"]
        query = operator_criteria["query"]

        if operator == self.__equals__:
            return {field+"__iexact":query}
        elif operator == self.__equals__:
            return {field+"__icontains":query}
        elif operator == self.__startswith__:
            return {field+"__istartswith":str(query)}
        elif operator == self.__endswith__:
            return {field+"__iendswith":str(query)}
        elif operator == self.__gt__:
            return {field+"__gt":str(query)}
        elif operator == self.__gte__:
            return {field+"__gte":str(query)}
        elif operator == self.__lt__:
            return {field+"__lt":str(query)}
        elif operator == self.__lte__:
            return {field+"__lte":str(query)}
        elif operator == self.__range__:
            return {field+"__range":tuple(query.split('|'))}
        return {}

    def get_query(self):
        query_filters = self._get_fragments()
        query = []
        for operator_type, filters in query_filters.items():
            if operator_type == "AND" and filters:
                query.append(reduce(operator.and_, [Q(**filter) for filter in filters if filter ]))
            elif operator_type == "OR" and filters:
                query.append(reduce(operator.or_, [Q(**filter) for filter in filters if filter]))
            elif operator_type == "NOT" and filters:
                query.append(reduce(operator.not_, [Q(**filter) for filter in filters if filter]))
        return query




