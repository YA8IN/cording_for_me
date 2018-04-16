class School:
    def __init__(self, name, year, address):
        self.name = name
        self.year = year
        self.address = address

school1 = School("송호고등학교", "1997", "안산시 상록구 이동" )
school2 = School("성안고등학교", "2000", "안산시 상록구 사1동" )
print(school1.name)
print(school2.address)
print(school2.year)
