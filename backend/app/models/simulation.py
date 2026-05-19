from datetime import datetime

from sqlalchemy import Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column,relationship


class Base(DeclarativeBase):
    pass

class MICCache(Base):
    __tablename__ = "mic_cache"

    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    molecule_chembl_id:Mapped[int] = mapped_column(String,index=True)
    standard_value: Mapped[float] = mapped_column(Float)
    standard_units: Mapped[str] = mapped_column(String)
    target_organism: Mapped[str] = mapped_column(String)
    fetched_at: Mapped[datetime] = mapped_column(DateTime,default=datetime.now)

    simulations: Mapped[list["Simulation"]] = relationship(back_populates="mic")

class Simulation(Base):
    __tablename__ = "simulation"

    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    antibiotic_name: Mapped[str] = mapped_column(String)
    molecule_chembl_id: Mapped[int] = mapped_column(String)
    concentration: Mapped[float] = mapped_column(Float)
    temperature: Mapped[float] = mapped_column(Float)
    environment_ph: Mapped[float] = mapped_column(Float)
    ecoli_strain: Mapped[str] = mapped_column(String)
    survival_rate: Mapped[float] = mapped_column(Float)
    resistance: Mapped[float] = mapped_column(Float)
    create_at: Mapped[datetime] = mapped_column(DateTime,default=datetime.now)

    mic_id: Mapped[int] = mapped_column(ForeignKey("mic_cache.mic_id"))
    mic: Mapped["MICCache"] = relationship(back_populates="simulations")