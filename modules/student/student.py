class student_details:
    def __init__(self):
        # student details
        self.full_name = ""
        self.date_of_birth = ""
        self.age = ""
        self.gender = ""
        self.mobile_number = ""
        self.email_address = ""
        self.password = ""
        self.preferred_language = ""
        self.school_college_name = ""
        self.class_grade = ""
        self.board_curriculum = ""
        self.academic_year = ""
        self.subjects_tution = []
        self.current_level_grade = {}
        self.areas_topic_help = []

        # parent/guardian details
        self.parent_guardian_name = ""
        self.relationship_with_student = ""
        self.parent_mobile_number = ""
        self.parent_email_address = ""
        self.preferred_communication_method = ""
    def setusernameandpassword(self, email, password):
        self.email_address = email
        self.password = password
    def set_student_details(self, full_name, date_of_birth, age, gender, mobile_number, preferred_language, school_college_name, class_grade, board_curriculum, academic_year):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.age = age
        self.gender = gender
        self.mobile_number = mobile_number
        self.preferred_language = preferred_language
        self.school_college_name = school_college_name
        self.class_grade = class_grade
        self.board_curriculum = board_curriculum
        self.academic_year = academic_year

    def save_basic_details_to_db(self):
        import sqlite3
        
        conn = sqlite3.connect("tution.db")

        
        cursor = conn.cursor()

        # Insert student details into the students table
        cursor.execute(
            """
            INSERT INTO students (
                full_name, date_of_birth, age, gender, mobile_number, email_address,
                password, preferred_language, school_college_name, class_grade,
                board_curriculam, academic_year
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
               self.full_name, self.date_of_birth, self.age, self.gender, self.mobile_number,
            self.email_address, self.password, self.preferred_language, self.school_college_name,
            self.class_grade, self.board_curriculum, self.academic_year),
        );

        conn.commit()   
        conn.close()    