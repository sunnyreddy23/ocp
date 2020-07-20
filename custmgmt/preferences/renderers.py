from core.renderers import CoreJSONRenderer

class TopicRenderer(CoreJSONRenderer):
    object_label = 'topic'
    pagination_object_label = 'topics'
    pagination_count_label = 'topicsCount'


class PreferenceRenderer(CoreJSONRenderer):
    object_label = 'preference'
    pagination_object_label = 'preferences'
    pagination_count_label = 'preferencesCount'

class MediumRenderer(CoreJSONRenderer):
    object_label = 'medium'
    pagination_object_label = 'mediums'
    pagination_count_label = 'mediumsCount'