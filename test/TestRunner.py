from unittest import TestLoader, TestSuite, TextTestRunner
from Signup import Signup
from Login import Login
from Forgotpassword import Forgotpassword
from Changepassword import Changepassword
from Searchhotels import Searchhotels
from ViewHotelsList import ViewHotelsList
from ViewHotelDetails import ViewHotelDetails
from ViewRoomDetails import ViewRoomDetails
from Bookroom import Bookroom
from Cancelroom import Cancelroom
from Downloadbookingdetails import Downloadbookingdetails
from AdminTest import AdminTest

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(Signup),
        loader.loadTestsFromTestCase(Forgotpassword),
        loader.loadTestsFromTestCase(Login),
        loader.loadTestsFromTestCase(Changepassword),
        loader.loadTestsFromTestCase(Searchhotels),
        loader.loadTestsFromTestCase(ViewHotelsList),
        loader.loadTestsFromTestCase(ViewHotelDetails),
        loader.loadTestsFromTestCase(ViewRoomDetails),
        loader.loadTestsFromTestCase(Bookroom),
        loader.loadTestsFromTestCase(Downloadbookingdetails),
        loader.loadTestsFromTestCase(Cancelroom),
        loader.loadTestsFromTestCase(AdminTest)
    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)