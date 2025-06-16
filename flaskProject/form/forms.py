"""Define WTForms-based survey forms for students and teachers."""

from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired


class StudentSurveyForm(FlaskForm):
    """
    Survey form for student users to indicate preferences and aspirations.

    Fields include:
    - Favorite subject
    - Learning style
    - Personal strengths
    - Desired future study area
    - Classroom behavior
    - Preferred extracurricular activities
    - Long-term goal
    """
    favorite_subject = RadioField('What is your favorite school subject?', choices=[
        ('math', 'Mathematics'),
        ('bulgarian', 'Bulgarian Language and Literature'),
        ('language', 'Foreign Language'),
        ('it', 'Informatics / IT'),
        ('history', 'History / Geography'),
        ('science', 'Biology / Chemistry'),
        ('arts', 'Arts')
    ], validators=[DataRequired()])

    learning_style = RadioField('How do you prefer to learn new things?', choices=[
        ('hands_on', 'Through hands-on tasks and experiments'),
        ('listening', 'By listening and taking notes'),
        ('reading', 'By reading independently'),
        ('discussion', 'In group discussions and teamwork')
    ], validators=[DataRequired()])

    strength = RadioField('What is your greatest strength?', choices=[
        ('logic', 'Logical thinking and analysis'),
        ('communication', 'Communication and expression'),
        ('creativity', 'Creativity and imagination'),
        ('organization', 'Organization and self-discipline'),
        ('tech', 'Working with technology')
    ], validators=[DataRequired()])

    future_study = RadioField('What do you want to study in the future?', choices=[
        ('programming', 'Programming / IT'),
        ('humanities', 'Languages and humanities'),
        ('sciences', 'Sciences'),
        ('arts', 'Arts / Design'),
        ('business', 'Business and economics'),
        ('undecided', 'I’m not sure yet')
    ], validators=[DataRequired()])

    class_behavior = RadioField('How would you describe yourself in the classroom?', choices=[
        ('active', 'Always an active participant'),
        ('thinker', 'I like to listen and reflect'),
        ('helper', 'I enjoy helping others'),
        ('independent', 'I prefer working independently')
    ], validators=[DataRequired()])

    activities = RadioField('What extracurricular activities do you enjoy the most?', choices=[
        ('competitions', 'Competitions in math, science, or programming'),
        ('journalism', 'Theater, writing, journalism'),
        ('artistic', 'Music, drawing, dancing'),
        ('volunteering', 'Volunteering, student council'),
        ('sports', 'Sports and physical activities')
    ], validators=[DataRequired()])

    goal = RadioField('What is your biggest goal after school?', choices=[
        ('abroad', 'To study abroad'),
        ('career', 'To start a career in a specific field'),
        ('entrepreneur', 'To start my own business'),
        ('discover', 'To discover my calling'),
        ('helping', 'To help people')
    ], validators=[DataRequired()])

    submit = SubmitField('Submit')


class TeacherSurveyForm(FlaskForm):
    """
    Survey form for teacher users to specify mentoring preferences and strengths.

    Fields include:
    - Favorite subjects to mentor
    - Teaching style
    - Mentoring strengths
    - Preferred student types
    - Favorite extracurricular focus
    - Mentorship goals
    """
    favorite_subjects_to_mentor = RadioField(
        'Which subject do you enjoy mentoring in the most?',
        choices=[
            ('math', 'Mathematics'),
            ('bulgarian', 'Bulgarian Language and Literature'),
            ('language', 'Foreign Languages'),
            ('it', 'Informatics / IT'),
            ('history', 'History / Geography'),
            ('science', 'Biology / Chemistry'),
            ('arts', 'Arts')
        ],
        validators=[DataRequired()]
    )

    teaching_style = RadioField(
        'What is your preferred teaching/mentoring style?',
        choices=[
            ('hands_on', 'Practical activities and demonstrations'),
            ('listening', 'Lectures and explanations'),
            ('reading', 'Assigning readings and discussion'),
            ('discussion', 'Collaborative discussions and teamwork')
        ],
        validators=[DataRequired()]
    )

    strengths = RadioField(
        'What is your strongest mentoring trait?',
        choices=[
            ('logic', 'Logical thinking and analysis'),
            ('communication', 'Communication and explanation'),
            ('creativity', 'Creativity and innovation'),
            ('organization', 'Structure and discipline'),
            ('tech', 'Using technology effectively')
        ],
        validators=[DataRequired()]
    )

    student_type_preference = RadioField(
        'What type of students do you work best with?',
        choices=[
            ('active', 'Highly active and engaged'),
            ('thinker', 'Reflective and thoughtful'),
            ('helper', 'Supportive and cooperative'),
            ('independent', 'Independent learners')
        ],
        validators=[DataRequired()]
    )

    extracurricular_focus = RadioField(
        'What kind of extracurricular mentoring do you enjoy most?',
        choices=[
            ('competitions', 'STEM competitions'),
            ('journalism', 'Writing, theatre, or journalism'),
            ('artistic', 'Music, art, or dance'),
            ('volunteering', 'Student council or volunteering'),
            ('sports', 'Sports and physical training')
        ],
        validators=[DataRequired()]
    )

    mentorship_goal = RadioField(
        'What is your primary goal as a mentor?',
        choices=[
            ('abroad', 'Help students apply abroad'),
            ('career', 'Guide toward specific careers'),
            ('entrepreneur', 'Support young entrepreneurs'),
            ('discover', 'Help them find their passion'),
            ('helping', 'Be a role model and helper')
        ],
        validators=[DataRequired()]
    )

    submit = SubmitField('Submit')