import uuid

from django.contrib.postgres.indexes import GinIndex, OpClass
from django.db import models
from django.db.models.functions import Cast, Upper


class Member(models.Model):
    uid = models.UUIDField(editable=False, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=256, db_index=True)
    external_id = models.CharField(max_length=64, db_index=True, blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(
                Upper("name"),
                name="name_upper_idx",
            ),
            GinIndex(
                OpClass(Upper("name"), name="gin_trgm_ops"), name="name_search_idx"
            ),
            GinIndex(OpClass("name", name="gin_trgm_ops"), name="name_gin_idx"),
            GinIndex(
                OpClass(
                    Upper(Cast("uid", output_field=models.TextField())),
                    name="gin_trgm_ops",
                ),
                name="uid_search_idx",
            ),
            models.Index(
                "name",
                name="name_no_external_id_idx",
                condition=models.Q(external_id__isnull=True),
            ),
        ]


class DocumentStatus(models.TextChoices):
    UNKNOWN = "unknown", "Unknown"
    VALID = "valid", "Valid"
    INVALID = "invalid", "Invalid"


class Document(models.Model):
    member = models.ForeignKey(Member, models.CASCADE)
    status = models.CharField(
        max_length=64,
        choices=DocumentStatus.choices,
        default=DocumentStatus.UNKNOWN,
        db_index=True,
    )
    data = models.JSONField(default=dict)

    class Meta:
        indexes = [
            models.Index(models.F("data__document_no"), name="data__document_no_idx"),
            GinIndex(
                OpClass(
                    Upper(
                        Cast(
                            models.F("data__document_no"),
                            output_field=models.TextField(),
                        )
                    ),
                    name="gin_trgm_ops",
                ),
                name="data__document_no_search_idx",
            ),
        ]
