"""
Utility functions for ML feature encoding.
"""

def encode_features(student, teacher):
    """
    Convert student and teacher attributes into a feature vector
    indicating compatibility.

    Args:
        student (StudentSurveyResponse): Student survey data.
        teacher (TeacherSurveyResponse): Teacher survey data.

    Returns:
        list[int]: Encoded features as binary values.
    """
    return [
        int(student.favorite_subject == teacher.favorite_subjects_to_mentor),
        int(student.learning_style == teacher.teaching_style),
        int(student.strength == teacher.strengths),
        int(student.class_behavior == teacher.student_type_preference),
        int(student.activities == teacher.extracurricular_focus),
        int(student.goal == teacher.mentorship_goal)
    ]