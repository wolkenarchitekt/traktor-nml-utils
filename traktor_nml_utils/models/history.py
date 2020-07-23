from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Head:
    """
    :ivar company:
    :ivar program:
    """
    class Meta:
        name = "HEAD"

    company: Optional[str] = field(
        default=None,
        metadata=dict(
            name="COMPANY",
            type="Attribute",
            required=True
        )
    )
    program: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PROGRAM",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Musicfolders:
    class Meta:
        name = "MUSICFOLDERS"


@dataclass
class Nml:
    """
    :ivar head:
    :ivar musicfolders:
    :ivar version:
    """
    class Meta:
        name = "NML"

    head: Optional[Head] = field(
        default=None,
        metadata=dict(
            name="HEAD",
            type="Element",
            required=True
        )
    )
    musicfolders: Optional[Musicfolders] = field(
        default=None,
        metadata=dict(
            name="MUSICFOLDERS",
            type="Element",
            required=True
        )
    )
    version: Optional[int] = field(
        default=None,
        metadata=dict(
            name="VERSION",
            type="Attribute",
            required=True
        )
    )
