# coding=utf-8
# pylint: disable=too-many-lines


from typing import List, TYPE_CHECKING, Union

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from . import models as _models
TodoLabel = Union[str, List[str], "_models.TodoLabelRecord", List["_models.TodoLabelRecord"]]
TodoAttachment = Union["_models.TodoFileAttachment", "_models.TodoUrlAttachment"]
