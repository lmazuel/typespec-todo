# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8

from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, List, Optional, TYPE_CHECKING, TypeVar, Union, overload

from corehttp.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime.pipeline import PipelineResponse
from corehttp.utils import case_insensitive_dict

from .. import models as _models
from .._model_base import SdkJSONEncoder, _deserialize
from .._serialization import Serializer

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import _types
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
_Unset: Any = object()
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_users_create_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/users"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_users_validate_request(*, token: str, **kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/validate"

    # Construct parameters
    _params["token"] = _SERIALIZER.query("token", token, "str")

    return HttpRequest(method="GET", url=_url, params=_params, **kwargs)


def build_users_login_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = "/login"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_users_logout_request(**kwargs: Any) -> HttpRequest:
    # Construct URL
    _url = "/logout"

    return HttpRequest(method="GET", url=_url, **kwargs)


def build_users_forgot_password_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = "/forgot-password"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_users_reset_password_request(*, reset_token: str, **kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/reset-password"

    # Construct parameters
    _params["resetToken"] = _SERIALIZER.query("reset_token", reset_token, "str")

    return HttpRequest(method="GET", url=_url, params=_params, **kwargs)


def build_todo_items_list_request(*, limit: int, offset: int, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/items"

    # Construct parameters
    _params["limit"] = _SERIALIZER.query("limit", limit, "int")
    _params["offset"] = _SERIALIZER.query("offset", offset, "int")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_todo_items_create_json_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("content-type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/items"

    # Construct headers
    if content_type is not None:
        _headers["content-type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_todo_items_create_form_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/items"

    # Construct headers
    if content_type is not None:
        _headers["content-type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_todo_items_get_request(id: int, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/items/{id}"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "int"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_todo_items_update_request(id: int, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("content-type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/items/{id}"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "int"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct headers
    if content_type is not None:
        _headers["content-type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PATCH", url=_url, headers=_headers, **kwargs)


def build_todo_items_delete_request(id: int, **kwargs: Any) -> HttpRequest:
    # Construct URL
    _url = "/items/{id}"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "int"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    return HttpRequest(method="DELETE", url=_url, **kwargs)


def build_todo_items_attachments_list_request(  # pylint: disable=name-too-long
    item_id: int, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/items/{itemId}/attachments"
    path_format_arguments = {
        "itemId": _SERIALIZER.url("item_id", item_id, "int"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_todo_items_attachments_create_url_attachment_request(  # pylint: disable=name-too-long
    item_id: int, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("content-type", None))
    # Construct URL
    _url = "/items/{itemId}/attachments"
    path_format_arguments = {
        "itemId": _SERIALIZER.url("item_id", item_id, "int"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct headers
    if content_type is not None:
        _headers["content-type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_todo_items_attachments_create_file_attachment_request(  # pylint: disable=name-too-long
    item_id: int, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    # Construct URL
    _url = "/items/{itemId}/attachments"
    path_format_arguments = {
        "itemId": _SERIALIZER.url("item_id", item_id, "int"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct headers
    if content_type is not None:
        _headers["content-type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


class UsersOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~brian.fun.service.TodoClient`'s
        :attr:`users` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def create(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> Union[
        _models.UserCreatedResponse,
        _models.UserExistsResponse,
        _models.InvalidUserResponse,
        _models.Standard4XXResponse,
        _models.Standard5XXResponse,
    ]:
        # pylint: disable=line-too-long
        """create.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: UserCreatedResponse or UserExistsResponse or InvalidUserResponse or
         Standard4XXResponse or Standard5XXResponse. The UserCreatedResponse is compatible with
         MutableMapping
        :rtype: ~brian.fun.service.models.UserCreatedResponse or
         ~brian.fun.service.models.UserExistsResponse or ~brian.fun.service.models.InvalidUserResponse
         or ~brian.fun.service.models.Standard4XXResponse or
         ~brian.fun.service.models.Standard5XXResponse
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "user": {
                        "email": "str",  # The user's email address. Required.
                        "id": 0,  # An autogenerated unique id for the user. Required.
                        "password": "str",  # The user's password, provided when creating a
                          user but is otherwise not visible (and hashed by the backend). Required.
                        "username": "str"  # The user's username. Required.
                    }
                }

                # response body for status code(s): 200
                response == {
                    "email": "str",  # The user's email address. Required.
                    "id": 0,  # An autogenerated unique id for the user. Required.
                    "password": "str",  # The user's password, provided when creating a user but
                      is otherwise not visible (and hashed by the backend). Required.
                    "token": "str",  # The token to use to construct the validate email address
                      url. Required.
                    "username": "str"  # The user's username. Required.
                }
                # response body for status code(s): 409, 422, 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """

    @overload
    def create(
        self, *, user: _models.User, content_type: str = "application/json", **kwargs: Any
    ) -> Union[
        _models.UserCreatedResponse,
        _models.UserExistsResponse,
        _models.InvalidUserResponse,
        _models.Standard4XXResponse,
        _models.Standard5XXResponse,
    ]:
        # pylint: disable=line-too-long
        """create.

        :keyword user: Required.
        :paramtype user: ~brian.fun.service.models.User
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: UserCreatedResponse or UserExistsResponse or InvalidUserResponse or
         Standard4XXResponse or Standard5XXResponse. The UserCreatedResponse is compatible with
         MutableMapping
        :rtype: ~brian.fun.service.models.UserCreatedResponse or
         ~brian.fun.service.models.UserExistsResponse or ~brian.fun.service.models.InvalidUserResponse
         or ~brian.fun.service.models.Standard4XXResponse or
         ~brian.fun.service.models.Standard5XXResponse
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "email": "str",  # The user's email address. Required.
                    "id": 0,  # An autogenerated unique id for the user. Required.
                    "password": "str",  # The user's password, provided when creating a user but
                      is otherwise not visible (and hashed by the backend). Required.
                    "token": "str",  # The token to use to construct the validate email address
                      url. Required.
                    "username": "str"  # The user's username. Required.
                }
                # response body for status code(s): 409, 422, 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """

    @overload
    def create(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> Union[
        _models.UserCreatedResponse,
        _models.UserExistsResponse,
        _models.InvalidUserResponse,
        _models.Standard4XXResponse,
        _models.Standard5XXResponse,
    ]:
        # pylint: disable=line-too-long
        """create.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: UserCreatedResponse or UserExistsResponse or InvalidUserResponse or
         Standard4XXResponse or Standard5XXResponse. The UserCreatedResponse is compatible with
         MutableMapping
        :rtype: ~brian.fun.service.models.UserCreatedResponse or
         ~brian.fun.service.models.UserExistsResponse or ~brian.fun.service.models.InvalidUserResponse
         or ~brian.fun.service.models.Standard4XXResponse or
         ~brian.fun.service.models.Standard5XXResponse
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "email": "str",  # The user's email address. Required.
                    "id": 0,  # An autogenerated unique id for the user. Required.
                    "password": "str",  # The user's password, provided when creating a user but
                      is otherwise not visible (and hashed by the backend). Required.
                    "token": "str",  # The token to use to construct the validate email address
                      url. Required.
                    "username": "str"  # The user's username. Required.
                }
                # response body for status code(s): 409, 422, 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """

    def create(
        self, body: Union[JSON, IO[bytes]] = _Unset, *, user: _models.User = _Unset, **kwargs: Any
    ) -> Union[
        _models.UserCreatedResponse,
        _models.UserExistsResponse,
        _models.InvalidUserResponse,
        _models.Standard4XXResponse,
        _models.Standard5XXResponse,
    ]:
        # pylint: disable=line-too-long
        """create.

        :param body: Is either a JSON type or a IO[bytes] type. Required.
        :type body: JSON or IO[bytes]
        :keyword user: Required.
        :paramtype user: ~brian.fun.service.models.User
        :return: UserCreatedResponse or UserExistsResponse or InvalidUserResponse or
         Standard4XXResponse or Standard5XXResponse. The UserCreatedResponse is compatible with
         MutableMapping
        :rtype: ~brian.fun.service.models.UserCreatedResponse or
         ~brian.fun.service.models.UserExistsResponse or ~brian.fun.service.models.InvalidUserResponse
         or ~brian.fun.service.models.Standard4XXResponse or
         ~brian.fun.service.models.Standard5XXResponse
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "user": {
                        "email": "str",  # The user's email address. Required.
                        "id": 0,  # An autogenerated unique id for the user. Required.
                        "password": "str",  # The user's password, provided when creating a
                          user but is otherwise not visible (and hashed by the backend). Required.
                        "username": "str"  # The user's username. Required.
                    }
                }

                # response body for status code(s): 200
                response == {
                    "email": "str",  # The user's email address. Required.
                    "id": 0,  # An autogenerated unique id for the user. Required.
                    "password": "str",  # The user's password, provided when creating a user but
                      is otherwise not visible (and hashed by the backend). Required.
                    "token": "str",  # The token to use to construct the validate email address
                      url. Required.
                    "username": "str"  # The user's username. Required.
                }
                # response body for status code(s): 409, 422, 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[
            Union[
                _models.UserCreatedResponse,
                _models.UserExistsResponse,
                _models.InvalidUserResponse,
                _models.Standard4XXResponse,
                _models.Standard5XXResponse,
            ]
        ] = kwargs.pop("cls", None)

        if body is _Unset:
            if user is _Unset:
                raise TypeError("missing required argument: user")
            body = {"user": user}
            body = {k: v for k, v in body.items() if v is not None}
        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_users_create_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 400, 409, 422, 500]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.status_code == 200:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.UserCreatedResponse, response.json())

        if response.status_code == 400:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard4XXResponse, response.json())

        if response.status_code == 409:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.UserExistsResponse, response.json())

        if response.status_code == 422:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.InvalidUserResponse, response.json())

        if response.status_code == 500:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard5XXResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def validate(
        self, *, token: str, **kwargs: Any
    ) -> Union[_models.InvalidUserResponse, _models.Standard4XXResponse, _models.Standard5XXResponse]:
        """validate.

        :keyword token: Required.
        :paramtype token: str
        :return: InvalidUserResponse or Standard4XXResponse or Standard5XXResponse or None. The
         InvalidUserResponse is compatible with MutableMapping
        :rtype: ~brian.fun.service.models.InvalidUserResponse or
         ~brian.fun.service.models.Standard4XXResponse or ~brian.fun.service.models.Standard5XXResponse
         or None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 422, 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[
            Union[_models.InvalidUserResponse, _models.Standard4XXResponse, _models.Standard5XXResponse]
        ] = kwargs.pop("cls", None)

        _request = build_users_validate_request(
            token=token,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204, 400, 422, 500]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 400:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard4XXResponse, response.json())

        if response.status_code == 422:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.InvalidUserResponse, response.json())

        if response.status_code == 500:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard5XXResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def login(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> Union[_models.Standard4XXResponse, _models.Standard5XXResponse]:
        """login.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Standard4XXResponse or Standard5XXResponse or None. The Standard4XXResponse is
         compatible with MutableMapping
        :rtype: ~brian.fun.service.models.Standard4XXResponse or
         ~brian.fun.service.models.Standard5XXResponse or None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "password": "str",  # Required.
                    "username": "str"  # Required.
                }

                # response body for status code(s): 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """

    @overload
    def login(
        self, *, username: str, password: str, content_type: str = "application/json", **kwargs: Any
    ) -> Union[_models.Standard4XXResponse, _models.Standard5XXResponse]:
        """login.

        :keyword username: Required.
        :paramtype username: str
        :keyword password: Required.
        :paramtype password: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Standard4XXResponse or Standard5XXResponse or None. The Standard4XXResponse is
         compatible with MutableMapping
        :rtype: ~brian.fun.service.models.Standard4XXResponse or
         ~brian.fun.service.models.Standard5XXResponse or None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """

    @overload
    def login(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> Union[_models.Standard4XXResponse, _models.Standard5XXResponse]:
        """login.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Standard4XXResponse or Standard5XXResponse or None. The Standard4XXResponse is
         compatible with MutableMapping
        :rtype: ~brian.fun.service.models.Standard4XXResponse or
         ~brian.fun.service.models.Standard5XXResponse or None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """

    def login(
        self, body: Union[JSON, IO[bytes]] = _Unset, *, username: str = _Unset, password: str = _Unset, **kwargs: Any
    ) -> Union[_models.Standard4XXResponse, _models.Standard5XXResponse]:
        """login.

        :param body: Is either a JSON type or a IO[bytes] type. Required.
        :type body: JSON or IO[bytes]
        :keyword username: Required.
        :paramtype username: str
        :keyword password: Required.
        :paramtype password: str
        :return: Standard4XXResponse or Standard5XXResponse or None. The Standard4XXResponse is
         compatible with MutableMapping
        :rtype: ~brian.fun.service.models.Standard4XXResponse or
         ~brian.fun.service.models.Standard5XXResponse or None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "password": "str",  # Required.
                    "username": "str"  # Required.
                }

                # response body for status code(s): 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[Union[_models.Standard4XXResponse, _models.Standard5XXResponse]] = kwargs.pop("cls", None)

        if body is _Unset:
            if username is _Unset:
                raise TypeError("missing required argument: username")
            if password is _Unset:
                raise TypeError("missing required argument: password")
            body = {"password": password, "username": username}
            body = {k: v for k, v in body.items() if v is not None}
        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_users_login_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204, 400, 401, 500]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 400:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard4XXResponse, response.json())

        if response.status_code == 500:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard5XXResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def logout(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """logout.

        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_users_logout_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def forgot_password(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> Union[_models.Standard4XXResponse, _models.Standard5XXResponse]:
        """Sends a reset token to the user's email address.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Standard4XXResponse or Standard5XXResponse or None. The Standard4XXResponse is
         compatible with MutableMapping
        :rtype: ~brian.fun.service.models.Standard4XXResponse or
         ~brian.fun.service.models.Standard5XXResponse or None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "email": "str"  # Required.
                }

                # response body for status code(s): 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """

    @overload
    def forgot_password(
        self, *, email: str, content_type: str = "application/json", **kwargs: Any
    ) -> Union[_models.Standard4XXResponse, _models.Standard5XXResponse]:
        """Sends a reset token to the user's email address.

        :keyword email: Required.
        :paramtype email: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Standard4XXResponse or Standard5XXResponse or None. The Standard4XXResponse is
         compatible with MutableMapping
        :rtype: ~brian.fun.service.models.Standard4XXResponse or
         ~brian.fun.service.models.Standard5XXResponse or None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """

    @overload
    def forgot_password(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> Union[_models.Standard4XXResponse, _models.Standard5XXResponse]:
        """Sends a reset token to the user's email address.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Standard4XXResponse or Standard5XXResponse or None. The Standard4XXResponse is
         compatible with MutableMapping
        :rtype: ~brian.fun.service.models.Standard4XXResponse or
         ~brian.fun.service.models.Standard5XXResponse or None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """

    def forgot_password(
        self, body: Union[JSON, IO[bytes]] = _Unset, *, email: str = _Unset, **kwargs: Any
    ) -> Union[_models.Standard4XXResponse, _models.Standard5XXResponse]:
        """Sends a reset token to the user's email address.

        :param body: Is either a JSON type or a IO[bytes] type. Required.
        :type body: JSON or IO[bytes]
        :keyword email: Required.
        :paramtype email: str
        :return: Standard4XXResponse or Standard5XXResponse or None. The Standard4XXResponse is
         compatible with MutableMapping
        :rtype: ~brian.fun.service.models.Standard4XXResponse or
         ~brian.fun.service.models.Standard5XXResponse or None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "email": "str"  # Required.
                }

                # response body for status code(s): 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[Union[_models.Standard4XXResponse, _models.Standard5XXResponse]] = kwargs.pop("cls", None)

        if body is _Unset:
            if email is _Unset:
                raise TypeError("missing required argument: email")
            body = {"email": email}
            body = {k: v for k, v in body.items() if v is not None}
        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_users_forgot_password_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204, 400, 404, 500]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 400:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard4XXResponse, response.json())

        if response.status_code == 500:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard5XXResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def reset_password(
        self, *, reset_token: str, **kwargs: Any
    ) -> Union[_models.Standard4XXResponse, _models.Standard5XXResponse]:
        """reset_password.

        :keyword reset_token: Required.
        :paramtype reset_token: str
        :return: Standard4XXResponse or Standard5XXResponse or None. The Standard4XXResponse is
         compatible with MutableMapping
        :rtype: ~brian.fun.service.models.Standard4XXResponse or
         ~brian.fun.service.models.Standard5XXResponse or None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[Union[_models.Standard4XXResponse, _models.Standard5XXResponse]] = kwargs.pop("cls", None)

        _request = build_users_reset_password_request(
            reset_token=reset_token,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204, 400, 404, 500]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 400:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard4XXResponse, response.json())

        if response.status_code == 500:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard5XXResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class TodoItemsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~brian.fun.service.TodoClient`'s
        :attr:`todo_items` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

        self.attachments = TodoItemsAttachmentsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def list(
        self, *, limit: int, offset: int, **kwargs: Any
    ) -> Union[_models.TodoPage, _models.Standard4XXResponse, _models.Standard5XXResponse]:
        # pylint: disable=line-too-long
        """list.

        :keyword limit: The limit to the number of items. Required.
        :paramtype limit: int
        :keyword offset: The offset to start paginating at. Required.
        :paramtype offset: int
        :return: TodoPage or Standard4XXResponse or Standard5XXResponse. The TodoPage is compatible
         with MutableMapping
        :rtype: ~brian.fun.service.models.TodoPage or ~brian.fun.service.models.Standard4XXResponse or
         ~brian.fun.service.models.Standard5XXResponse
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "items": [
                        {
                            "completedAt": "2020-02-20 00:00:00",  # When the todo item
                              was makred as completed. Required.
                            "createdAt": "2020-02-20 00:00:00",  # When the todo item was
                              created. Required.
                            "createdBy": 0,  # User that created the todo. Required.
                            "id": 0,  # The item's unique id. Required.
                            "labels": [
                                "str"  # Required.
                            ],
                            "status": "NotStarted",  # Default value is "NotStarted". The
                              status of the todo item. Required. Is one of the following types:
                              Literal["NotStarted"], Literal["InProgress"], Literal["Completed"]
                            "title": "str",  # The item's title. Required.
                            "updatedAt": "2020-02-20 00:00:00",  # When the todo item was
                              last updated. Required.
                            "assignedTo": 0,  # Optional. User that the todo is assigned
                              to.
                            "description": "str"  # Optional. A longer description of the
                              todo item in markdown format.
                        }
                    ],
                    "pagination": {
                        "pageSize": 0,  # The number of items returned in this page.
                          Required.
                        "totalSize": 0,  # The total number of items. Required.
                        "nextLink": "str",  # Optional. A link to the next page, if it
                          exists.
                        "prevLink": "str"  # Optional. A link to the previous page, if it
                          exists.
                    }
                }
                # response body for status code(s): 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[Union[_models.TodoPage, _models.Standard4XXResponse, _models.Standard5XXResponse]] = kwargs.pop(
            "cls", None
        )

        _request = build_todo_items_list_request(
            limit=limit,
            offset=offset,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 400, 500]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.status_code == 200:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.TodoPage, response.json())

        if response.status_code == 400:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard4XXResponse, response.json())

        if response.status_code == 500:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard5XXResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def create_json(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> Union[_models.TodoItem, _models.InvalidTodoItem, _models.Standard4XXResponse, _models.Standard5XXResponse]:
        # pylint: disable=line-too-long
        """create_json.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: TodoItem or InvalidTodoItem or Standard4XXResponse or Standard5XXResponse. The
         TodoItem is compatible with MutableMapping
        :rtype: ~brian.fun.service.models.TodoItem or ~brian.fun.service.models.InvalidTodoItem or
         ~brian.fun.service.models.Standard4XXResponse or ~brian.fun.service.models.Standard5XXResponse
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "attachments": [
                        {
                            "contents": bytes("bytes", encoding="utf-8"),  # The contents
                              of the file. Required.
                            "filename": "str",  # The file name of the attachment.
                              Required.
                            "mediaType": "str",  # The media type of the attachment.
                              Required.
                            "todoItemId": 0,  # The todo item this is attached to.
                              Required.
                            "url": "str"  # The url where the attachment can be
                              downloaded from. Required.
                        }
                    ],
                    "item": {
                        "completedAt": "2020-02-20 00:00:00",  # When the todo item was
                          makred as completed. Required.
                        "createdAt": "2020-02-20 00:00:00",  # When the todo item was
                          created. Required.
                        "createdBy": 0,  # User that created the todo. Required.
                        "id": 0,  # The item's unique id. Required.
                        "labels": [
                            "str"  # Required.
                        ],
                        "status": "NotStarted",  # Default value is "NotStarted". The status
                          of the todo item. Required. Is one of the following types:
                          Literal["NotStarted"], Literal["InProgress"], Literal["Completed"]
                        "title": "str",  # The item's title. Required.
                        "updatedAt": "2020-02-20 00:00:00",  # When the todo item was last
                          updated. Required.
                        "assignedTo": 0,  # Optional. User that the todo is assigned to.
                        "description": "str"  # Optional. A longer description of the todo
                          item in markdown format.
                    }
                }

                # response body for status code(s): 200
                response == {
                    "completedAt": "2020-02-20 00:00:00",  # When the todo item was makred as
                      completed. Required.
                    "createdAt": "2020-02-20 00:00:00",  # When the todo item was created.
                      Required.
                    "createdBy": 0,  # User that created the todo. Required.
                    "id": 0,  # The item's unique id. Required.
                    "labels": [
                        "str"  # Required.
                    ],
                    "status": "NotStarted",  # Default value is "NotStarted". The status of the
                      todo item. Required. Is one of the following types: Literal["NotStarted"],
                      Literal["InProgress"], Literal["Completed"]
                    "title": "str",  # The item's title. Required.
                    "updatedAt": "2020-02-20 00:00:00",  # When the todo item was last updated.
                      Required.
                    "assignedTo": 0,  # Optional. User that the todo is assigned to.
                    "description": "str"  # Optional. A longer description of the todo item in
                      markdown format.
                }
                # response body for status code(s): 422, 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """

    @overload
    def create_json(
        self,
        *,
        item: _models.TodoItem,
        attachments: List["_types.TodoAttachment"],
        content_type: str = "application/json",
        **kwargs: Any
    ) -> Union[_models.TodoItem, _models.InvalidTodoItem, _models.Standard4XXResponse, _models.Standard5XXResponse]:
        # pylint: disable=line-too-long
        """create_json.

        :keyword item: Required.
        :paramtype item: ~brian.fun.service.models.TodoItem
        :keyword attachments: Required.
        :paramtype attachments: list[~brian.fun.service.models.TodoFileAttachment or
         ~brian.fun.service.models.TodoUrlAttachment]
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: TodoItem or InvalidTodoItem or Standard4XXResponse or Standard5XXResponse. The
         TodoItem is compatible with MutableMapping
        :rtype: ~brian.fun.service.models.TodoItem or ~brian.fun.service.models.InvalidTodoItem or
         ~brian.fun.service.models.Standard4XXResponse or ~brian.fun.service.models.Standard5XXResponse
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "completedAt": "2020-02-20 00:00:00",  # When the todo item was makred as
                      completed. Required.
                    "createdAt": "2020-02-20 00:00:00",  # When the todo item was created.
                      Required.
                    "createdBy": 0,  # User that created the todo. Required.
                    "id": 0,  # The item's unique id. Required.
                    "labels": [
                        "str"  # Required.
                    ],
                    "status": "NotStarted",  # Default value is "NotStarted". The status of the
                      todo item. Required. Is one of the following types: Literal["NotStarted"],
                      Literal["InProgress"], Literal["Completed"]
                    "title": "str",  # The item's title. Required.
                    "updatedAt": "2020-02-20 00:00:00",  # When the todo item was last updated.
                      Required.
                    "assignedTo": 0,  # Optional. User that the todo is assigned to.
                    "description": "str"  # Optional. A longer description of the todo item in
                      markdown format.
                }
                # response body for status code(s): 422, 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """

    @overload
    def create_json(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> Union[_models.TodoItem, _models.InvalidTodoItem, _models.Standard4XXResponse, _models.Standard5XXResponse]:
        # pylint: disable=line-too-long
        """create_json.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: TodoItem or InvalidTodoItem or Standard4XXResponse or Standard5XXResponse. The
         TodoItem is compatible with MutableMapping
        :rtype: ~brian.fun.service.models.TodoItem or ~brian.fun.service.models.InvalidTodoItem or
         ~brian.fun.service.models.Standard4XXResponse or ~brian.fun.service.models.Standard5XXResponse
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "completedAt": "2020-02-20 00:00:00",  # When the todo item was makred as
                      completed. Required.
                    "createdAt": "2020-02-20 00:00:00",  # When the todo item was created.
                      Required.
                    "createdBy": 0,  # User that created the todo. Required.
                    "id": 0,  # The item's unique id. Required.
                    "labels": [
                        "str"  # Required.
                    ],
                    "status": "NotStarted",  # Default value is "NotStarted". The status of the
                      todo item. Required. Is one of the following types: Literal["NotStarted"],
                      Literal["InProgress"], Literal["Completed"]
                    "title": "str",  # The item's title. Required.
                    "updatedAt": "2020-02-20 00:00:00",  # When the todo item was last updated.
                      Required.
                    "assignedTo": 0,  # Optional. User that the todo is assigned to.
                    "description": "str"  # Optional. A longer description of the todo item in
                      markdown format.
                }
                # response body for status code(s): 422, 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """

    def create_json(
        self,
        body: Union[JSON, IO[bytes]] = _Unset,
        *,
        item: _models.TodoItem = _Unset,
        attachments: List["_types.TodoAttachment"] = _Unset,
        **kwargs: Any
    ) -> Union[_models.TodoItem, _models.InvalidTodoItem, _models.Standard4XXResponse, _models.Standard5XXResponse]:
        # pylint: disable=line-too-long
        """create_json.

        :param body: Is either a JSON type or a IO[bytes] type. Required.
        :type body: JSON or IO[bytes]
        :keyword item: Required.
        :paramtype item: ~brian.fun.service.models.TodoItem
        :keyword attachments: Required.
        :paramtype attachments: list[~brian.fun.service.models.TodoFileAttachment or
         ~brian.fun.service.models.TodoUrlAttachment]
        :return: TodoItem or InvalidTodoItem or Standard4XXResponse or Standard5XXResponse. The
         TodoItem is compatible with MutableMapping
        :rtype: ~brian.fun.service.models.TodoItem or ~brian.fun.service.models.InvalidTodoItem or
         ~brian.fun.service.models.Standard4XXResponse or ~brian.fun.service.models.Standard5XXResponse
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "attachments": [
                        {
                            "contents": bytes("bytes", encoding="utf-8"),  # The contents
                              of the file. Required.
                            "filename": "str",  # The file name of the attachment.
                              Required.
                            "mediaType": "str",  # The media type of the attachment.
                              Required.
                            "todoItemId": 0,  # The todo item this is attached to.
                              Required.
                            "url": "str"  # The url where the attachment can be
                              downloaded from. Required.
                        }
                    ],
                    "item": {
                        "completedAt": "2020-02-20 00:00:00",  # When the todo item was
                          makred as completed. Required.
                        "createdAt": "2020-02-20 00:00:00",  # When the todo item was
                          created. Required.
                        "createdBy": 0,  # User that created the todo. Required.
                        "id": 0,  # The item's unique id. Required.
                        "labels": [
                            "str"  # Required.
                        ],
                        "status": "NotStarted",  # Default value is "NotStarted". The status
                          of the todo item. Required. Is one of the following types:
                          Literal["NotStarted"], Literal["InProgress"], Literal["Completed"]
                        "title": "str",  # The item's title. Required.
                        "updatedAt": "2020-02-20 00:00:00",  # When the todo item was last
                          updated. Required.
                        "assignedTo": 0,  # Optional. User that the todo is assigned to.
                        "description": "str"  # Optional. A longer description of the todo
                          item in markdown format.
                    }
                }

                # response body for status code(s): 200
                response == {
                    "completedAt": "2020-02-20 00:00:00",  # When the todo item was makred as
                      completed. Required.
                    "createdAt": "2020-02-20 00:00:00",  # When the todo item was created.
                      Required.
                    "createdBy": 0,  # User that created the todo. Required.
                    "id": 0,  # The item's unique id. Required.
                    "labels": [
                        "str"  # Required.
                    ],
                    "status": "NotStarted",  # Default value is "NotStarted". The status of the
                      todo item. Required. Is one of the following types: Literal["NotStarted"],
                      Literal["InProgress"], Literal["Completed"]
                    "title": "str",  # The item's title. Required.
                    "updatedAt": "2020-02-20 00:00:00",  # When the todo item was last updated.
                      Required.
                    "assignedTo": 0,  # Optional. User that the todo is assigned to.
                    "description": "str"  # Optional. A longer description of the todo item in
                      markdown format.
                }
                # response body for status code(s): 422, 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("content-type", None))
        cls: ClsType[
            Union[_models.TodoItem, _models.InvalidTodoItem, _models.Standard4XXResponse, _models.Standard5XXResponse]
        ] = kwargs.pop("cls", None)

        if body is _Unset:
            if item is _Unset:
                raise TypeError("missing required argument: item")
            if attachments is _Unset:
                raise TypeError("missing required argument: attachments")
            body = {"attachments": attachments, "item": item}
            body = {k: v for k, v in body.items() if v is not None}
        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_todo_items_create_json_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 400, 422, 500]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.status_code == 200:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.TodoItem, response.json())

        if response.status_code == 400:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard4XXResponse, response.json())

        if response.status_code == 422:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.InvalidTodoItem, response.json())

        if response.status_code == 500:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard5XXResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def create_form(
        self, body: JSON, **kwargs: Any
    ) -> Union[_models.TodoItem, _models.InvalidTodoItem, _models.Standard4XXResponse, _models.Standard5XXResponse]:
        # pylint: disable=line-too-long
        """create_form.

        :param body: Required.
        :type body: JSON
        :return: TodoItem or InvalidTodoItem or Standard4XXResponse or Standard5XXResponse. The
         TodoItem is compatible with MutableMapping
        :rtype: ~brian.fun.service.models.TodoItem or ~brian.fun.service.models.InvalidTodoItem or
         ~brian.fun.service.models.Standard4XXResponse or ~brian.fun.service.models.Standard5XXResponse
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "item": {
                        "completedAt": "2020-02-20 00:00:00",  # When the todo item was
                          makred as completed. Required.
                        "createdAt": "2020-02-20 00:00:00",  # When the todo item was
                          created. Required.
                        "createdBy": 0,  # User that created the todo. Required.
                        "id": 0,  # The item's unique id. Required.
                        "labels": [
                            "str"  # Required.
                        ],
                        "status": "NotStarted",  # Default value is "NotStarted". The status
                          of the todo item. Required. Is one of the following types:
                          Literal["NotStarted"], Literal["InProgress"], Literal["Completed"]
                        "title": "str",  # The item's title. Required.
                        "updatedAt": "2020-02-20 00:00:00",  # When the todo item was last
                          updated. Required.
                        "assignedTo": 0,  # Optional. User that the todo is assigned to.
                        "description": "str"  # Optional. A longer description of the todo
                          item in markdown format.
                    },
                    "attachments": [
                        {
                            "description": "str",  # A description of the URL. Required.
                            "url": "str"  # The url. Required.
                        }
                    ]
                }

                # response body for status code(s): 200
                response == {
                    "completedAt": "2020-02-20 00:00:00",  # When the todo item was makred as
                      completed. Required.
                    "createdAt": "2020-02-20 00:00:00",  # When the todo item was created.
                      Required.
                    "createdBy": 0,  # User that created the todo. Required.
                    "id": 0,  # The item's unique id. Required.
                    "labels": [
                        "str"  # Required.
                    ],
                    "status": "NotStarted",  # Default value is "NotStarted". The status of the
                      todo item. Required. Is one of the following types: Literal["NotStarted"],
                      Literal["InProgress"], Literal["Completed"]
                    "title": "str",  # The item's title. Required.
                    "updatedAt": "2020-02-20 00:00:00",  # When the todo item was last updated.
                      Required.
                    "assignedTo": 0,  # Optional. User that the todo is assigned to.
                    "description": "str"  # Optional. A longer description of the todo item in
                      markdown format.
                }
                # response body for status code(s): 422, 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """

    @overload
    def create_form(
        self,
        *,
        item: _models.TodoItem,
        attachments: Optional[List[Union[_models.TodoUrlAttachment, bytes]]] = None,
        **kwargs: Any
    ) -> Union[_models.TodoItem, _models.InvalidTodoItem, _models.Standard4XXResponse, _models.Standard5XXResponse]:
        # pylint: disable=line-too-long
        """create_form.

        :keyword item: Required.
        :paramtype item: ~brian.fun.service.models.TodoItem
        :keyword attachments: Default value is None.
        :paramtype attachments: list[~brian.fun.service.models.TodoUrlAttachment or bytes]
        :return: TodoItem or InvalidTodoItem or Standard4XXResponse or Standard5XXResponse. The
         TodoItem is compatible with MutableMapping
        :rtype: ~brian.fun.service.models.TodoItem or ~brian.fun.service.models.InvalidTodoItem or
         ~brian.fun.service.models.Standard4XXResponse or ~brian.fun.service.models.Standard5XXResponse
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "completedAt": "2020-02-20 00:00:00",  # When the todo item was makred as
                      completed. Required.
                    "createdAt": "2020-02-20 00:00:00",  # When the todo item was created.
                      Required.
                    "createdBy": 0,  # User that created the todo. Required.
                    "id": 0,  # The item's unique id. Required.
                    "labels": [
                        "str"  # Required.
                    ],
                    "status": "NotStarted",  # Default value is "NotStarted". The status of the
                      todo item. Required. Is one of the following types: Literal["NotStarted"],
                      Literal["InProgress"], Literal["Completed"]
                    "title": "str",  # The item's title. Required.
                    "updatedAt": "2020-02-20 00:00:00",  # When the todo item was last updated.
                      Required.
                    "assignedTo": 0,  # Optional. User that the todo is assigned to.
                    "description": "str"  # Optional. A longer description of the todo item in
                      markdown format.
                }
                # response body for status code(s): 422, 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """

    def create_form(
        self,
        body: JSON = _Unset,
        *,
        item: _models.TodoItem = _Unset,
        attachments: Optional[List[Union[_models.TodoUrlAttachment, bytes]]] = None,
        **kwargs: Any
    ) -> Union[_models.TodoItem, _models.InvalidTodoItem, _models.Standard4XXResponse, _models.Standard5XXResponse]:
        # pylint: disable=line-too-long
        """create_form.

        :param body: Is one of the following types: JSON Required.
        :type body: JSON
        :keyword item: Required.
        :paramtype item: ~brian.fun.service.models.TodoItem
        :keyword attachments: Default value is None.
        :paramtype attachments: list[~brian.fun.service.models.TodoUrlAttachment or bytes]
        :return: TodoItem or InvalidTodoItem or Standard4XXResponse or Standard5XXResponse. The
         TodoItem is compatible with MutableMapping
        :rtype: ~brian.fun.service.models.TodoItem or ~brian.fun.service.models.InvalidTodoItem or
         ~brian.fun.service.models.Standard4XXResponse or ~brian.fun.service.models.Standard5XXResponse
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "item": {
                        "completedAt": "2020-02-20 00:00:00",  # When the todo item was
                          makred as completed. Required.
                        "createdAt": "2020-02-20 00:00:00",  # When the todo item was
                          created. Required.
                        "createdBy": 0,  # User that created the todo. Required.
                        "id": 0,  # The item's unique id. Required.
                        "labels": [
                            "str"  # Required.
                        ],
                        "status": "NotStarted",  # Default value is "NotStarted". The status
                          of the todo item. Required. Is one of the following types:
                          Literal["NotStarted"], Literal["InProgress"], Literal["Completed"]
                        "title": "str",  # The item's title. Required.
                        "updatedAt": "2020-02-20 00:00:00",  # When the todo item was last
                          updated. Required.
                        "assignedTo": 0,  # Optional. User that the todo is assigned to.
                        "description": "str"  # Optional. A longer description of the todo
                          item in markdown format.
                    },
                    "attachments": [
                        {
                            "description": "str",  # A description of the URL. Required.
                            "url": "str"  # The url. Required.
                        }
                    ]
                }

                # response body for status code(s): 200
                response == {
                    "completedAt": "2020-02-20 00:00:00",  # When the todo item was makred as
                      completed. Required.
                    "createdAt": "2020-02-20 00:00:00",  # When the todo item was created.
                      Required.
                    "createdBy": 0,  # User that created the todo. Required.
                    "id": 0,  # The item's unique id. Required.
                    "labels": [
                        "str"  # Required.
                    ],
                    "status": "NotStarted",  # Default value is "NotStarted". The status of the
                      todo item. Required. Is one of the following types: Literal["NotStarted"],
                      Literal["InProgress"], Literal["Completed"]
                    "title": "str",  # The item's title. Required.
                    "updatedAt": "2020-02-20 00:00:00",  # When the todo item was last updated.
                      Required.
                    "assignedTo": 0,  # Optional. User that the todo is assigned to.
                    "description": "str"  # Optional. A longer description of the todo item in
                      markdown format.
                }
                # response body for status code(s): 422, 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[
            Union[_models.TodoItem, _models.InvalidTodoItem, _models.Standard4XXResponse, _models.Standard5XXResponse]
        ] = kwargs.pop("cls", None)

        if body is _Unset:
            if item is _Unset:
                raise TypeError("missing required argument: item")
            body = {"attachments": attachments, "item": item}
            body = {k: v for k, v in body.items() if v is not None}
        content_type = content_type or "multipart/form-data"
        _content = None
        if isinstance(body, MutableMapping):
            _content = body
        elif isinstance(body, MutableMapping):
            _content = body

        _request = build_todo_items_create_form_request(
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 400, 422, 500]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.status_code == 200:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.TodoItem, response.json())

        if response.status_code == 400:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard4XXResponse, response.json())

        if response.status_code == 422:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.InvalidTodoItem, response.json())

        if response.status_code == 500:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard5XXResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def get(self, id: int, **kwargs: Any) -> Optional[_models.TodoItem]:
        # pylint: disable=line-too-long
        """get.

        :param id: Required.
        :type id: int
        :return: TodoItem or None. The TodoItem is compatible with MutableMapping
        :rtype: ~brian.fun.service.models.TodoItem or None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "completedAt": "2020-02-20 00:00:00",  # When the todo item was makred as
                      completed. Required.
                    "createdAt": "2020-02-20 00:00:00",  # When the todo item was created.
                      Required.
                    "createdBy": 0,  # User that created the todo. Required.
                    "id": 0,  # The item's unique id. Required.
                    "labels": [
                        "str"  # Required.
                    ],
                    "status": "NotStarted",  # Default value is "NotStarted". The status of the
                      todo item. Required. Is one of the following types: Literal["NotStarted"],
                      Literal["InProgress"], Literal["Completed"]
                    "title": "str",  # The item's title. Required.
                    "updatedAt": "2020-02-20 00:00:00",  # When the todo item was last updated.
                      Required.
                    "assignedTo": 0,  # Optional. User that the todo is assigned to.
                    "description": "str"  # Optional. A longer description of the todo item in
                      markdown format.
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[Optional[_models.TodoItem]] = kwargs.pop("cls", None)

        _request = build_todo_items_get_request(
            id=id,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 404]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.TodoItem, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def update(
        self, id: int, body: JSON, *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.TodoItem:
        # pylint: disable=line-too-long
        """update.

        :param id: Required.
        :type id: int
        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: TodoItem. The TodoItem is compatible with MutableMapping
        :rtype: ~brian.fun.service.models.TodoItem
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "patch": {
                        "assignedTo": 0,  # Optional. User that the todo is assigned to.
                        "description": "str",  # Optional. A longer description of the todo
                          item in markdown format.
                        "status": "NotStarted",  # Optional. Default value is "NotStarted".
                          The status of the todo item. Is one of the following types:
                          Literal["NotStarted"], Literal["InProgress"], Literal["Completed"]
                        "title": "str"  # Optional. The item's title.
                    }
                }

                # response body for status code(s): 200
                response == {
                    "completedAt": "2020-02-20 00:00:00",  # When the todo item was makred as
                      completed. Required.
                    "createdAt": "2020-02-20 00:00:00",  # When the todo item was created.
                      Required.
                    "createdBy": 0,  # User that created the todo. Required.
                    "id": 0,  # The item's unique id. Required.
                    "labels": [
                        "str"  # Required.
                    ],
                    "status": "NotStarted",  # Default value is "NotStarted". The status of the
                      todo item. Required. Is one of the following types: Literal["NotStarted"],
                      Literal["InProgress"], Literal["Completed"]
                    "title": "str",  # The item's title. Required.
                    "updatedAt": "2020-02-20 00:00:00",  # When the todo item was last updated.
                      Required.
                    "assignedTo": 0,  # Optional. User that the todo is assigned to.
                    "description": "str"  # Optional. A longer description of the todo item in
                      markdown format.
                }
        """

    @overload
    def update(
        self,
        id: int,
        *,
        patch: _models.TodoItemPatch,
        content_type: str = "application/merge-patch+json",
        **kwargs: Any
    ) -> _models.TodoItem:
        # pylint: disable=line-too-long
        """update.

        :param id: Required.
        :type id: int
        :keyword patch: Required.
        :paramtype patch: ~brian.fun.service.models.TodoItemPatch
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: TodoItem. The TodoItem is compatible with MutableMapping
        :rtype: ~brian.fun.service.models.TodoItem
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "completedAt": "2020-02-20 00:00:00",  # When the todo item was makred as
                      completed. Required.
                    "createdAt": "2020-02-20 00:00:00",  # When the todo item was created.
                      Required.
                    "createdBy": 0,  # User that created the todo. Required.
                    "id": 0,  # The item's unique id. Required.
                    "labels": [
                        "str"  # Required.
                    ],
                    "status": "NotStarted",  # Default value is "NotStarted". The status of the
                      todo item. Required. Is one of the following types: Literal["NotStarted"],
                      Literal["InProgress"], Literal["Completed"]
                    "title": "str",  # The item's title. Required.
                    "updatedAt": "2020-02-20 00:00:00",  # When the todo item was last updated.
                      Required.
                    "assignedTo": 0,  # Optional. User that the todo is assigned to.
                    "description": "str"  # Optional. A longer description of the todo item in
                      markdown format.
                }
        """

    @overload
    def update(
        self, id: int, body: IO[bytes], *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.TodoItem:
        # pylint: disable=line-too-long
        """update.

        :param id: Required.
        :type id: int
        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: TodoItem. The TodoItem is compatible with MutableMapping
        :rtype: ~brian.fun.service.models.TodoItem
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "completedAt": "2020-02-20 00:00:00",  # When the todo item was makred as
                      completed. Required.
                    "createdAt": "2020-02-20 00:00:00",  # When the todo item was created.
                      Required.
                    "createdBy": 0,  # User that created the todo. Required.
                    "id": 0,  # The item's unique id. Required.
                    "labels": [
                        "str"  # Required.
                    ],
                    "status": "NotStarted",  # Default value is "NotStarted". The status of the
                      todo item. Required. Is one of the following types: Literal["NotStarted"],
                      Literal["InProgress"], Literal["Completed"]
                    "title": "str",  # The item's title. Required.
                    "updatedAt": "2020-02-20 00:00:00",  # When the todo item was last updated.
                      Required.
                    "assignedTo": 0,  # Optional. User that the todo is assigned to.
                    "description": "str"  # Optional. A longer description of the todo item in
                      markdown format.
                }
        """

    def update(
        self, id: int, body: Union[JSON, IO[bytes]] = _Unset, *, patch: _models.TodoItemPatch = _Unset, **kwargs: Any
    ) -> _models.TodoItem:
        # pylint: disable=line-too-long
        """update.

        :param id: Required.
        :type id: int
        :param body: Is either a JSON type or a IO[bytes] type. Required.
        :type body: JSON or IO[bytes]
        :keyword patch: Required.
        :paramtype patch: ~brian.fun.service.models.TodoItemPatch
        :return: TodoItem. The TodoItem is compatible with MutableMapping
        :rtype: ~brian.fun.service.models.TodoItem
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "patch": {
                        "assignedTo": 0,  # Optional. User that the todo is assigned to.
                        "description": "str",  # Optional. A longer description of the todo
                          item in markdown format.
                        "status": "NotStarted",  # Optional. Default value is "NotStarted".
                          The status of the todo item. Is one of the following types:
                          Literal["NotStarted"], Literal["InProgress"], Literal["Completed"]
                        "title": "str"  # Optional. The item's title.
                    }
                }

                # response body for status code(s): 200
                response == {
                    "completedAt": "2020-02-20 00:00:00",  # When the todo item was makred as
                      completed. Required.
                    "createdAt": "2020-02-20 00:00:00",  # When the todo item was created.
                      Required.
                    "createdBy": 0,  # User that created the todo. Required.
                    "id": 0,  # The item's unique id. Required.
                    "labels": [
                        "str"  # Required.
                    ],
                    "status": "NotStarted",  # Default value is "NotStarted". The status of the
                      todo item. Required. Is one of the following types: Literal["NotStarted"],
                      Literal["InProgress"], Literal["Completed"]
                    "title": "str",  # The item's title. Required.
                    "updatedAt": "2020-02-20 00:00:00",  # When the todo item was last updated.
                      Required.
                    "assignedTo": 0,  # Optional. User that the todo is assigned to.
                    "description": "str"  # Optional. A longer description of the todo item in
                      markdown format.
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("content-type", None))
        cls: ClsType[_models.TodoItem] = kwargs.pop("cls", None)

        if body is _Unset:
            if patch is _Unset:
                raise TypeError("missing required argument: patch")
            body = {"patch": patch}
            body = {k: v for k, v in body.items() if v is not None}
        content_type = content_type or "application/merge-patch+json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_todo_items_update_request(
            id=id,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.TodoItem, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def delete(self, id: int, **kwargs: Any) -> Union[_models.Standard4XXResponse, _models.Standard5XXResponse]:
        """delete.

        :param id: Required.
        :type id: int
        :return: Standard4XXResponse or Standard5XXResponse or None. The Standard4XXResponse is
         compatible with MutableMapping
        :rtype: ~brian.fun.service.models.Standard4XXResponse or
         ~brian.fun.service.models.Standard5XXResponse or None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[Union[_models.Standard4XXResponse, _models.Standard5XXResponse]] = kwargs.pop("cls", None)

        _request = build_todo_items_delete_request(
            id=id,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204, 400, 404, 500]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 400:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard4XXResponse, response.json())

        if response.status_code == 500:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard5XXResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class TodoItemsAttachmentsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~brian.fun.service.TodoClient`'s
        :attr:`attachments` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    def list(
        self, item_id: int, **kwargs: Any
    ) -> Union[List["_types.TodoAttachment"], _models.Standard4XXResponse, _models.Standard5XXResponse]:
        """list.

        :param item_id: Required.
        :type item_id: int
        :return: list of TodoFileAttachment or TodoUrlAttachment or Standard4XXResponse or
         Standard5XXResponse or None. The Standard4XXResponse is compatible with MutableMapping
        :rtype: list[~brian.fun.service.models.TodoFileAttachment or
         ~brian.fun.service.models.TodoUrlAttachment] or ~brian.fun.service.models.Standard4XXResponse
         or ~brian.fun.service.models.Standard5XXResponse or None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == [
                    {
                        "contents": bytes("bytes", encoding="utf-8"),  # The contents of the
                          file. Required.
                        "filename": "str",  # The file name of the attachment. Required.
                        "mediaType": "str",  # The media type of the attachment. Required.
                        "todoItemId": 0,  # The todo item this is attached to. Required.
                        "url": "str"  # The url where the attachment can be downloaded from.
                          Required.
                    }
                ]
                # response body for status code(s): 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[
            Union[List["_types.TodoAttachment"], _models.Standard4XXResponse, _models.Standard5XXResponse]
        ] = kwargs.pop("cls", None)

        _request = build_todo_items_attachments_list_request(
            item_id=item_id,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 400, 404, 500]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(List["_types.TodoAttachment"], response.json())

        if response.status_code == 400:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard4XXResponse, response.json())

        if response.status_code == 500:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard5XXResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def create_url_attachment(
        self, item_id: int, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> Union[_models.Standard4XXResponse, _models.Standard5XXResponse]:
        """create_url_attachment.

        :param item_id: Required.
        :type item_id: int
        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Standard4XXResponse or Standard5XXResponse or None. The Standard4XXResponse is
         compatible with MutableMapping
        :rtype: ~brian.fun.service.models.Standard4XXResponse or
         ~brian.fun.service.models.Standard5XXResponse or None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "contents": {
                        "contents": bytes("bytes", encoding="utf-8"),  # The contents of the
                          file. Required.
                        "filename": "str",  # The file name of the attachment. Required.
                        "mediaType": "str",  # The media type of the attachment. Required.
                        "todoItemId": 0,  # The todo item this is attached to. Required.
                        "url": "str"  # The url where the attachment can be downloaded from.
                          Required.
                    }
                }

                # response body for status code(s): 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """

    @overload
    def create_url_attachment(
        self, item_id: int, *, contents: "_types.TodoAttachment", content_type: str = "application/json", **kwargs: Any
    ) -> Union[_models.Standard4XXResponse, _models.Standard5XXResponse]:
        """create_url_attachment.

        :param item_id: Required.
        :type item_id: int
        :keyword contents: Is either a TodoFileAttachment type or a TodoUrlAttachment type. Required.
        :paramtype contents: ~brian.fun.service.models.TodoFileAttachment or
         ~brian.fun.service.models.TodoUrlAttachment
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Standard4XXResponse or Standard5XXResponse or None. The Standard4XXResponse is
         compatible with MutableMapping
        :rtype: ~brian.fun.service.models.Standard4XXResponse or
         ~brian.fun.service.models.Standard5XXResponse or None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """

    @overload
    def create_url_attachment(
        self, item_id: int, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> Union[_models.Standard4XXResponse, _models.Standard5XXResponse]:
        """create_url_attachment.

        :param item_id: Required.
        :type item_id: int
        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Standard4XXResponse or Standard5XXResponse or None. The Standard4XXResponse is
         compatible with MutableMapping
        :rtype: ~brian.fun.service.models.Standard4XXResponse or
         ~brian.fun.service.models.Standard5XXResponse or None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """

    def create_url_attachment(
        self,
        item_id: int,
        body: Union[JSON, IO[bytes]] = _Unset,
        *,
        contents: "_types.TodoAttachment" = _Unset,
        **kwargs: Any
    ) -> Union[_models.Standard4XXResponse, _models.Standard5XXResponse]:
        """create_url_attachment.

        :param item_id: Required.
        :type item_id: int
        :param body: Is either a JSON type or a IO[bytes] type. Required.
        :type body: JSON or IO[bytes]
        :keyword contents: Is either a TodoFileAttachment type or a TodoUrlAttachment type. Required.
        :paramtype contents: ~brian.fun.service.models.TodoFileAttachment or
         ~brian.fun.service.models.TodoUrlAttachment
        :return: Standard4XXResponse or Standard5XXResponse or None. The Standard4XXResponse is
         compatible with MutableMapping
        :rtype: ~brian.fun.service.models.Standard4XXResponse or
         ~brian.fun.service.models.Standard5XXResponse or None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "contents": {
                        "contents": bytes("bytes", encoding="utf-8"),  # The contents of the
                          file. Required.
                        "filename": "str",  # The file name of the attachment. Required.
                        "mediaType": "str",  # The media type of the attachment. Required.
                        "todoItemId": 0,  # The todo item this is attached to. Required.
                        "url": "str"  # The url where the attachment can be downloaded from.
                          Required.
                    }
                }

                # response body for status code(s): 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("content-type", None))
        cls: ClsType[Union[_models.Standard4XXResponse, _models.Standard5XXResponse]] = kwargs.pop("cls", None)

        if body is _Unset:
            if contents is _Unset:
                raise TypeError("missing required argument: contents")
            body = {"contents": contents}
            body = {k: v for k, v in body.items() if v is not None}
        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_todo_items_attachments_create_url_attachment_request(
            item_id=item_id,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204, 400, 404, 500]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 400:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard4XXResponse, response.json())

        if response.status_code == 500:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard5XXResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def create_file_attachment(
        self, item_id: int, body: JSON, **kwargs: Any
    ) -> Union[_models.Standard4XXResponse, _models.Standard5XXResponse]:
        """create_file_attachment.

        :param item_id: Required.
        :type item_id: int
        :param body: Required.
        :type body: JSON
        :return: Standard4XXResponse or Standard5XXResponse or None. The Standard4XXResponse is
         compatible with MutableMapping
        :rtype: ~brian.fun.service.models.Standard4XXResponse or
         ~brian.fun.service.models.Standard5XXResponse or None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "contents": bytes("bytes", encoding="utf-8")  # Required.
                }

                # response body for status code(s): 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """

    @overload
    def create_file_attachment(
        self, item_id: int, *, contents: bytes, **kwargs: Any
    ) -> Union[_models.Standard4XXResponse, _models.Standard5XXResponse]:
        """create_file_attachment.

        :param item_id: Required.
        :type item_id: int
        :keyword contents: Required.
        :paramtype contents: bytes
        :return: Standard4XXResponse or Standard5XXResponse or None. The Standard4XXResponse is
         compatible with MutableMapping
        :rtype: ~brian.fun.service.models.Standard4XXResponse or
         ~brian.fun.service.models.Standard5XXResponse or None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """

    def create_file_attachment(
        self, item_id: int, body: JSON = _Unset, *, contents: bytes = _Unset, **kwargs: Any
    ) -> Union[_models.Standard4XXResponse, _models.Standard5XXResponse]:
        """create_file_attachment.

        :param item_id: Required.
        :type item_id: int
        :param body: Is one of the following types: JSON Required.
        :type body: JSON
        :keyword contents: Required.
        :paramtype contents: bytes
        :return: Standard4XXResponse or Standard5XXResponse or None. The Standard4XXResponse is
         compatible with MutableMapping
        :rtype: ~brian.fun.service.models.Standard4XXResponse or
         ~brian.fun.service.models.Standard5XXResponse or None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "contents": bytes("bytes", encoding="utf-8")  # Required.
                }

                # response body for status code(s): 400, 500
                response == {
                    "code": "str",  # A machine readable error code. Required.
                    "message": "str"  # A human readable message. Required.
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[Union[_models.Standard4XXResponse, _models.Standard5XXResponse]] = kwargs.pop("cls", None)

        if body is _Unset:
            if contents is _Unset:
                raise TypeError("missing required argument: contents")
            body = {"contents": contents}
            body = {k: v for k, v in body.items() if v is not None}
        content_type = content_type or "multipart/form-data"
        _content = None
        if isinstance(body, MutableMapping):
            _content = body
        elif isinstance(body, MutableMapping):
            _content = body

        _request = build_todo_items_attachments_create_file_attachment_request(
            item_id=item_id,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204, 400, 404, 500]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 400:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard4XXResponse, response.json())

        if response.status_code == 500:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.Standard5XXResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
