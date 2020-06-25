from periodically.tasks import PeriodicTask
from periodically import register
from periodically.schedules import Daily
from main.models import Reservation, Loan
from datetime import date

class ReservationToLoan(PeriodicTask):
    def run(self):
        for reservation in Reservation.objects.all():
            if reservation.reservationStartDate == date.today():
                if reservation.reservedItem.itemAvailable == True:
                    newLoan = Loan(
                        loanedItem = reservation.reservedItem,
                        loanStartDate = reservation.reservationStartDate,
                        loanEndDate = reservation.reservationEndDate,
                        loaningUser = reservation.reservedFor,
                        loanPurpose = reservation.reservationPurpose
                    )

                    newLoan.save()




# Run task daily
register.task(ReservationToLoan(), Daily())