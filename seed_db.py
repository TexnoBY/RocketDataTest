from django_seed import Seed
from staff.models import Position, Employer, TeamLeader, DepartmentLeader, VicePresident, President

seeder = Seed.seeder()

seeder.add_entity(Position, 15)
seeder.add_entity(Employer, 15)
seeder.add_entity(TeamLeader, 15)
seeder.add_entity(DepartmentLeader, 15)
seeder.add_entity(VicePresident, 15)
seeder.add_entity(President, 15)

inserted_pks = seeder.execute()

