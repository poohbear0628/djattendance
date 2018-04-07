from accounts.models import TrainingAssistant
from aputils.utils import get_or_none


TA_PAIRINGS = {
    get_or_none(TrainingAssistant, lastname="Chumreonlert"): get_or_none(TrainingAssistant, lastname="Hale"),
    get_or_none(TrainingAssistant, lastname="Miao"): get_or_none(TrainingAssistant, lastname="Bang"),
    get_or_none(TrainingAssistant, lastname="Macaranas"): get_or_none(TrainingAssistant, lastname="Deng"),
    get_or_none(TrainingAssistant, lastname="Buntain"): get_or_none(TrainingAssistant, lastname="Li"),
    get_or_none(TrainingAssistant, lastname="Uy"): get_or_none(TrainingAssistant, lastname="Li"),
}
