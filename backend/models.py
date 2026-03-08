from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    workouts = relationship('Workout', back_populates='user')

class Workout(Base):
    __tablename__ = 'workouts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    exercises = relationship('TemplateExercise', back_populates='workout')
    user = relationship('User', back_populates='workouts')

class Exercise(Base):
    __tablename__ = 'exercises'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class WorkoutTemplate(Base):
    __tablename__ = 'workout_templates'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    exercises = relationship('TemplateExercise', back_populates='template')

class TemplateExercise(Base):
    __tablename__ = 'template_exercises'
    id = Column(Integer, primary_key=True)
    workout_template_id = Column(Integer, ForeignKey('workout_templates.id'), nullable=False)
    exercise_id = Column(Integer, ForeignKey('exercises.id'), nullable=False)
    sets = Column(Integer, nullable=False)
    reps = Column(Integer, nullable=False)
    weight = Column(Integer)
    RPE = Column(Integer)
    rest_period_seconds = Column(Integer)
    exercise_duration_seconds = Column(Integer)
    template = relationship('WorkoutTemplate', back_populates='exercises')
    exercise = relationship('Exercise')
