from datetime import datetime

from sqlalchemy.orm import relationship

from webapp.db import db


class Case(db.Model):
    __tablename__ = "case"
    id = db.Column(db.Integer, primary_key=True)
    number_case = db.Column(db.String, unique=True, nullable=False)
    applicant = db.Column(db.String, nullable=False)
    type_applicant = db.Column(db.Integer, db.ForeignKey('type_applicant.id'))
    appraiser = db.Column(db.String, nullable=True)
    judge = db.Column(db.String, nullable=True)
    status_case = db.Column(db.Integer, db.ForeignKey('status_case.id'))
    comment = db.Column(db.String, nullable=True)

    def status_case_description(self):
        status = StatusCase.query.filter(StatusCase.id == self.status_case).first()
        return status.description

    def count_objects(self):
        return RealtyObject.query.filter(RealtyObject.number_case == self.number_case).count()

    def count_documents(self):
        return Document.query.filter(Document.number_case == self.number_case).count()

    def __repr__(self):
        return f'Case: {self.number_case}, id: {self.id}>'


class RealtyObject(db.Model):
    __tablename__ = "realty_object"
    id = db.Column(db.Integer, primary_key=True)
    cadastral_number = db.Column(db.String, nullable=False, index=True)
    type_realty = db.Column(db.Integer, db.ForeignKey('type_realty.id'))
    category = db.Column(db.String, db.ForeignKey('categories.id'))
    article = db.Column(db.String, nullable=True)
    current_cadastral_cost = db.Column(db.Float, nullable=True)
    new_cadastral_cost = db.Column(db.Float, nullable=True)
    approved_cadastral_cost = db.Column(db.Float, nullable=True)
    segment = db.Column(db.Integer, nullable=True)
    codervi = db.Column(db.String, nullable=True)
    number_case = db.Column(db.String, db.ForeignKey('case.number_case'), index=True)

    case = relationship('Case', backref='objects')

    def __repr__(self):
        return f'<Realty object: {self.cadastral_number} for case {self.number_case}>'


class Document(db.Model):
    __tablename__ = "documents"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    number = db.Column(db.String, nullable=True)
    date = db.Column(db.String, nullable=True)
    type = db.Column(db.Integer, db.ForeignKey('type_document.id'))
    url = db.Column(db.String, nullable=False)
    extension = db.Column(db.String, nullable=True)
    size = db.Column(db.Integer, nullable=True)
    comment = db.Column(db.String, nullable=True)
    number_case = db.Column(db.String, db.ForeignKey('case.number_case'), index=True)
    expert = db.Column(db.String, nullable=True)
    type_examination = db.Column(db.String, nullable=True)
    parent_document = db.Column(db.Integer, nullable=True)

    case = relationship('Case', backref='documents')

    def __repr__(self):
        return f'<Document: {self.title} for case {self.number_case}>'


class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=True)
    comment = db.Column(db.String, nullable=True)
    number_case = db.Column(db.String, db.ForeignKey('case.number_case'), index=True)

    case = relationship('Case', backref='events')

    @property
    def fdate(self):
        return datetime.strptime(self.date, '%Y-%m-%d').strftime('%d.%m.%Y')

    @property
    def ftime(self):
        if self.time is None:
            return ''
        return self.time

    def __repr__(self):
        return f'<Event: {self.date} for case {self.number_case}>'


class Categories(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=True)
    description_lite = db.Column(db.String, nullable=True)
    type_realty = db.Column(db.String, db.ForeignKey('type_realty.id'))

    def __repr__(self):
        return f'Category: {self.id}, {self.description}>'


class TypeApplicant(db.Model):
    __tablename__ = "type_applicant"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'Type applicant: {self.id}, {self.description}>'


class TypeDocument(db.Model):
    __tablename__ = "type_document"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'Type document: {self.id}, {self.description}>'


class TypeRealty(db.Model):
    __tablename__ = "type_realty"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'Type realty: {self.id}, {self.description}>'


class StatusCase(db.Model):
    __tablename__ = "status_case"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'Status case: {self.id}, {self.description}>'
