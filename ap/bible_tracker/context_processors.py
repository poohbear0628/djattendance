from .utils import bible_reading_finalized


def bible_tracker_forced(request):
    forced = not bible_reading_finalized(request.user)  # forced if bible reading not finalized
    return {'bible_tracker_forced': forced}
