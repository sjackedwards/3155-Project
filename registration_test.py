import unittest
from authentication import register, login, check_password_requirements
from database import setup_database, cleanup_test_user

class TestAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        setup_database()
        cleanup_test_user()

    def test_check_password_requirements(self):
        print("\nTest: Checking password requirements")

        print("  Test Case 1: Valid password")
        self.assertTrue(check_password_requirements("A5tr0n0m3r"), "Valid password should be accepted.")

        print("  Test Case 2: Password with too few characters")
        self.assertFalse(check_password_requirements("short"), "Password with too few characters should be rejected.")

        print("  Test Case 3: Password without uppercase")
        self.assertFalse(check_password_requirements("onlylowercase"), "Password without uppercase should be rejected.")

        print("  Test Case 4: Password without lowercase")
        self.assertFalse(check_password_requirements("ONLYUPPERCASE"), "Password without lowercase should be rejected.")

        print("Test: Checking password requirements - PASSED")

    def test_register_login(self):
        print("\nTest: Registration and Login")

        print("  Test Case 1: Registration with a new user")
        self.assertTrue(register("testuser", "Testpassword1"), "Registration with a new user should be successful.")
        print("  Test Case 1: PASSED")

        print("  Test Case 2: Registration with an existing user")
        self.assertFalse(register("testuser", "Testpassword1"), "Registration with an existing user should be rejected.")
        print("  Test Case 2: PASSED")

        print("  Test Case 3: Login with correct credentials")
        self.assertIsNotNone(login("testuser", "Testpassword1"), "Login with correct credentials should be successful.")
        print("  Test Case 3: PASSED")

        print("  Test Case 4: Login with incorrect username")
        self.assertIsNone(login("wronguser", "Testpassword1"), "Login with incorrect username should be rejected.")
        print("  Test Case 4: PASSED")

        print("  Test Case 5: Login with incorrect password")
        self.assertIsNone(login("testuser", "wrongpassword"), "Login with incorrect password should be rejected.")
        print("  Test Case 5: PASSED")

        print("  Test Case 6: Login with empty username")
        self.assertIsNone(login("", "testpassword"), "Login with empty username should be rejected.")
        print("  Test Case 6: PASSED")

        print("  Test Case 7: Login with empty password")
        self.assertIsNone(login("testuser", ""), "Login with empty password should be rejected.")
        print("  Test Case 7: PASSED")

        print("Test: Registration and Login - PASSED")

    @classmethod
    def tearDownClass(cls):
        cleanup_test_user()

def main():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAuth)
    unittest.TextTestRunner(verbosity=1).run(suite)

if __name__ == '__main__':
    main()
