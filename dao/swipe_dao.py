from models import Swipe
from db import db
from datetime import date

class swipe_dao:
    @classmethod
    def get_all_by_uid(cls, user_id):
        return Swipe.query.filter_by(swiper_id=user_id).all()

    @classmethod
    def create_swipe(cls, swiper_id, swiped_id, swipe_type, match_generated=False):
        swipe = Swipe(
            swiper_id=swiper_id,
            swiped_id=swiped_id,
            swipe_type=swipe_type,
            swiped_at=date.today(),
            #match_generated=match_generated raus genommen wegen Fehler
        )
        db.session.add(swipe)
        db.session.commit()
        return swipe