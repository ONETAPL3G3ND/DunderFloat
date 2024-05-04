class User:

    def __init__(self):
        self.WeeklyActivity = [True, False, False, True, True, True, False]

    def __float__(self):
        return self.WeeklyActivity.count(True) / self.WeeklyActivity.count(False)

    def GetActivityCoefficient(self):
        return float(self)

if __name__ == "__main__":
    user = User()
    print(user.GetActivityCoefficient())