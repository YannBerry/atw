from modeltranslation.translator import translator, TranslationOptions
from atw.map.models import Trip, TripStage, Country, Type, Massif


class CountryTranslationOptions(TranslationOptions):
    fields = ('country',)


class TypeTranslationOptions(TranslationOptions):
    fields = ('type',)


class MassifTranslationOptions(TranslationOptions):
    fields = ('massif',)


class TripTranslationOptions(TranslationOptions):
    fields = ('trip_name', 'trip_slug', 'description',)


class TripStageTranslationOptions(TranslationOptions):
    fields = ('stage_name', 'stage_slug', 'story',)


translator.register(Country, CountryTranslationOptions)
translator.register(Type, TypeTranslationOptions)
translator.register(Massif, MassifTranslationOptions)
translator.register(Trip, TripTranslationOptions)
translator.register(TripStage, TripStageTranslationOptions)