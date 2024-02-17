# coding=utf-8


from copy import deepcopy
from typing import Any, Awaitable

from corehttp.credentials import ServiceKeyCredential
from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime import AsyncPipelineClient, policies

from .._serialization import Deserializer, Serializer
from ._configuration import TodoClientConfiguration
from .operations import TodoItemsOperations, UsersOperations


class TodoClient:  # pylint: disable=client-accepts-api-version-keyword
    """TodoClient.

    :ivar users: UsersOperations operations
    :vartype users: brian.fun.service.aio.operations.UsersOperations
    :ivar todo_items: TodoItemsOperations operations
    :vartype todo_items: brian.fun.service.aio.operations.TodoItemsOperations
    :param credential: Credential needed for the client to connect to cloud service. Required.
    :type credential: ~corehttp.credentials.ServiceKeyCredential
    :keyword endpoint: Service host. Required.
    :paramtype endpoint: str
    """

    def __init__(self, credential: ServiceKeyCredential, *, endpoint: str, **kwargs: Any) -> None:
        self._config = TodoClientConfiguration(credential=credential, **kwargs)
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.logging_policy,
            ]
        self._client: AsyncPipelineClient = AsyncPipelineClient(endpoint=endpoint, policies=_policies, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.users = UsersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.todo_items = TodoItemsOperations(self._client, self._config, self._serialize, self._deserialize)

    def send_request(
        self, request: HttpRequest, *, stream: bool = False, **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from corehttp.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~corehttp.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~corehttp.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "TodoClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
