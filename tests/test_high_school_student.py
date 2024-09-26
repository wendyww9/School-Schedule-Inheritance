from school_schedule.high_school_student import HighSchoolStudent

def test_new_valid_high_school_student_with_defaults():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = HighSchoolStudent(name, grade, classes)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert not ellis.has_parking_privileges
    assert not ellis.clubs

def test_new_valid_high_school_student_with_all_attributes():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = HighSchoolStudent(name, grade, classes,
        has_parking_privileges=True,
        clubs=["Film Club"])

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert ellis.has_parking_privileges
    assert len(ellis.clubs) == 1

def test_add_class():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]
    new_class = "Writing"

    # Act
    ellis = HighSchoolStudent(name, grade, classes)
    ellis.add_class(new_class)

    # Assert
    assert len(ellis.classes) == 2

def test_join_club():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]
    new_club = "Cat Fanciers Club"

    # Act
    ellis = HighSchoolStudent(name, grade, classes)
    ellis.join_club(new_club)

    # Assert
    assert len(ellis.clubs) == 1

def test_get_num_classes():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting", "Writing"]
    ellis = HighSchoolStudent(name, grade, classes)

    # Act
    num_classes = ellis.get_num_classes()

    # Assert
    assert num_classes == 2

def test_high_school_student_summary_with_parking_and_clubs():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = []

    # Act
    ellis = HighSchoolStudent(name, grade, classes,
        has_parking_privileges=True,
        clubs=["DJ Club"])
    summary = ellis.summary()

    assert summary == "Ellis is a junior enrolled in 0 classes: \nEllis has parking privileges\nEllis is a member of: DJ Club"

def test_high_school_student_summary_without_parking_or_clubs():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = []

    # Act
    ellis = HighSchoolStudent(name, grade, classes)
    summary = ellis.summary()

    assert summary == "Ellis is a junior enrolled in 0 classes: \nEllis doesn't have parking privileges\nEllis hasn't joined a club yet."
