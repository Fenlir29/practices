class Student:
    
    def __init__(self, name, section, spanish, english, social, science):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social = social
        self.science = science
    
    def calculate_average(self):
        total = self.spanish + self.english + self.social + self.science
        average = total / 4
        return average
    
    def get_failing_subjects(self):
       
        failing = []
        if self.spanish < 60:
            failing.append(('Spanish', self.spanish))
        if self.english < 60:
            failing.append(('English', self.english))
        if self.social < 60:
            failing.append(('Social Studies', self.social))
        if self.science < 60:
            failing.append(('Science', self.science))
        return failing
    
    def is_passing(self):
        
        return self.calculate_average() >= 70
    
    def to_dict(self):
        
        return {
            'name': self.name,
            'section': self.section,
            'spanish': self.spanish,
            'english': self.english,
            'social': self.social,
            'science': self.science
        }
    def from_dict(data):
      
        return Student(
            name=data.get('name', '').strip(),
            section=data.get('section', '').strip().upper(),
            spanish=float(data.get('spanish', 0)),
            english=float(data.get('english', 0)),
            social=float(data.get('social', 0)),
            science=float(data.get('science', 0))
        )
    
   