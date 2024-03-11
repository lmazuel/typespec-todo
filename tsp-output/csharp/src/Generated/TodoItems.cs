// <auto-generated/>

#nullable disable

using System;
using System.ClientModel;
using System.ClientModel.Internal;
using System.ClientModel.Primitives;
using System.ClientModel.Primitives.Pipeline;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;
using Todo.Models;

namespace Todo
{
    // Data plane generated sub-client.
    /// <summary> The TodoItems sub-client. </summary>
    public partial class TodoItems
    {
        private const string AuthorizationHeader = "session-id";
        private readonly KeyCredential _keyCredential;
        private readonly MessagePipeline _pipeline;

        /// <summary> The ClientDiagnostics is used to provide tracing support for the client library. </summary>
        internal TelemetrySource ClientDiagnostics { get; }

        /// <summary> The HTTP pipeline for sending and receiving REST requests and responses. </summary>
        public virtual MessagePipeline Pipeline => _pipeline;

        /// <summary> Initializes a new instance of TodoItems for mocking. </summary>
        protected TodoItems()
        {
        }

        /// <summary> Initializes a new instance of TodoItems. </summary>
        /// <param name="clientDiagnostics"> The handler for diagnostic messaging in the client. </param>
        /// <param name="pipeline"> The HTTP pipeline for sending and receiving REST requests and responses. </param>
        /// <param name="keyCredential"> The key credential to copy. </param>
        internal TodoItems(TelemetrySource clientDiagnostics, MessagePipeline pipeline, KeyCredential keyCredential)
        {
            ClientDiagnostics = clientDiagnostics;
            _pipeline = pipeline;
            _keyCredential = keyCredential;
        }

        /// <param name="limit"> The limit to the number of items. </param>
        /// <param name="offset"> The offset to start paginating at. </param>
        /// <param name="cancellationToken"> The cancellation token to use. </param>
        public virtual async Task<Result<TodoPage>> GetTodoItemsAsync(int? limit = null, int? offset = null, CancellationToken cancellationToken = default)
        {
            RequestOptions context = FromCancellationToken(cancellationToken);
            Result result = await GetTodoItemsAsync(limit, offset, context).ConfigureAwait(false);
            return Result.FromValue(TodoPage.FromResponse(result.GetRawResponse()), result.GetRawResponse());
        }

        /// <param name="limit"> The limit to the number of items. </param>
        /// <param name="offset"> The offset to start paginating at. </param>
        /// <param name="cancellationToken"> The cancellation token to use. </param>
        public virtual Result<TodoPage> GetTodoItems(int? limit = null, int? offset = null, CancellationToken cancellationToken = default)
        {
            RequestOptions context = FromCancellationToken(cancellationToken);
            Result result = GetTodoItems(limit, offset, context);
            return Result.FromValue(TodoPage.FromResponse(result.GetRawResponse()), result.GetRawResponse());
        }

        /// <summary>
        /// [Protocol Method]
        /// <list type="bullet">
        /// <item>
        /// <description>
        /// This <see href="https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/core/Azure.Core/samples/ProtocolMethods.md">protocol method</see> allows explicit creation of the request and processing of the response for advanced scenarios.
        /// </description>
        /// </item>
        /// <item>
        /// <description>
        /// Please try the simpler <see cref="GetTodoItemsAsync(int?,int?,CancellationToken)"/> convenience overload with strongly typed models first.
        /// </description>
        /// </item>
        /// </list>
        /// </summary>
        /// <param name="limit"> The limit to the number of items. </param>
        /// <param name="offset"> The offset to start paginating at. </param>
        /// <param name="context"> The request context, which can override default behaviors of the client pipeline on a per-call basis. </param>
        /// <exception cref="MessageFailedException"> Service returned a non-success status code. </exception>
        /// <returns> The response returned from the service. </returns>
        public virtual async Task<Result> GetTodoItemsAsync(int? limit, int? offset, RequestOptions context)
        {
            using var scope = ClientDiagnostics.CreateSpan("TodoItems.GetTodoItems");
            scope.Start();
            try
            {
                using PipelineMessage message = CreateGetTodoItemsRequest(limit, offset, context);
                return Result.FromResponse(await _pipeline.ProcessMessageAsync(message, context).ConfigureAwait(false));
            }
            catch (Exception e)
            {
                scope.Failed(e);
                throw;
            }
        }

        /// <summary>
        /// [Protocol Method]
        /// <list type="bullet">
        /// <item>
        /// <description>
        /// This <see href="https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/core/Azure.Core/samples/ProtocolMethods.md">protocol method</see> allows explicit creation of the request and processing of the response for advanced scenarios.
        /// </description>
        /// </item>
        /// <item>
        /// <description>
        /// Please try the simpler <see cref="GetTodoItems(int?,int?,CancellationToken)"/> convenience overload with strongly typed models first.
        /// </description>
        /// </item>
        /// </list>
        /// </summary>
        /// <param name="limit"> The limit to the number of items. </param>
        /// <param name="offset"> The offset to start paginating at. </param>
        /// <param name="context"> The request context, which can override default behaviors of the client pipeline on a per-call basis. </param>
        /// <exception cref="MessageFailedException"> Service returned a non-success status code. </exception>
        /// <returns> The response returned from the service. </returns>
        public virtual Result GetTodoItems(int? limit, int? offset, RequestOptions context)
        {
            using var scope = ClientDiagnostics.CreateSpan("TodoItems.GetTodoItems");
            scope.Start();
            try
            {
                using PipelineMessage message = CreateGetTodoItemsRequest(limit, offset, context);
                return Result.FromResponse(_pipeline.ProcessMessage(message, context));
            }
            catch (Exception e)
            {
                scope.Failed(e);
                throw;
            }
        }

        /// <param name="item"></param>
        /// <param name="attachments"></param>
        /// <param name="cancellationToken"> The cancellation token to use. </param>
        /// <exception cref="ArgumentNullException"> <paramref name="item"/> is null. </exception>
        public virtual async Task<Result<TodoItem>> CreateAsync(TodoItem item, IEnumerable<BinaryData> attachments = null, CancellationToken cancellationToken = default)
        {
            Argument.AssertNotNull(item, nameof(item));

            RequestOptions context = FromCancellationToken(cancellationToken);
            CreateRequest createRequest = new CreateRequest(item);
            if (attachments != null)
            {
                foreach (var value in attachments)
                {
                    createRequest.Attachments.Add(value);
                }
            }
            CreateRequest createRequest0 = createRequest;
            Result result = await CreateAsync(createRequest0.ToRequestBody(), context).ConfigureAwait(false);
            return Result.FromValue(TodoItem.FromResponse(result.GetRawResponse()), result.GetRawResponse());
        }

        /// <param name="item"></param>
        /// <param name="attachments"></param>
        /// <param name="cancellationToken"> The cancellation token to use. </param>
        /// <exception cref="ArgumentNullException"> <paramref name="item"/> is null. </exception>
        public virtual Result<TodoItem> Create(TodoItem item, IEnumerable<BinaryData> attachments = null, CancellationToken cancellationToken = default)
        {
            Argument.AssertNotNull(item, nameof(item));

            RequestOptions context = FromCancellationToken(cancellationToken);
            CreateRequest createRequest = new CreateRequest(item);
            if (attachments != null)
            {
                foreach (var value in attachments)
                {
                    createRequest.Attachments.Add(value);
                }
            }
            CreateRequest createRequest0 = createRequest;
            Result result = Create(createRequest0.ToRequestBody(), context);
            return Result.FromValue(TodoItem.FromResponse(result.GetRawResponse()), result.GetRawResponse());
        }

        /// <summary>
        /// [Protocol Method]
        /// <list type="bullet">
        /// <item>
        /// <description>
        /// This <see href="https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/core/Azure.Core/samples/ProtocolMethods.md">protocol method</see> allows explicit creation of the request and processing of the response for advanced scenarios.
        /// </description>
        /// </item>
        /// <item>
        /// <description>
        /// Please try the simpler <see cref="CreateAsync(TodoItem,IEnumerable{BinaryData},CancellationToken)"/> convenience overload with strongly typed models first.
        /// </description>
        /// </item>
        /// </list>
        /// </summary>
        /// <param name="content"> The content to send as the body of the request. </param>
        /// <param name="context"> The request context, which can override default behaviors of the client pipeline on a per-call basis. </param>
        /// <exception cref="ArgumentNullException"> <paramref name="content"/> is null. </exception>
        /// <exception cref="MessageFailedException"> Service returned a non-success status code. </exception>
        /// <returns> The response returned from the service. </returns>
        public virtual async Task<Result> CreateAsync(RequestBody content, RequestOptions context = null)
        {
            Argument.AssertNotNull(content, nameof(content));

            using var scope = ClientDiagnostics.CreateSpan("TodoItems.Create");
            scope.Start();
            try
            {
                using PipelineMessage message = CreateCreateRequest(content, context);
                return Result.FromResponse(await _pipeline.ProcessMessageAsync(message, context).ConfigureAwait(false));
            }
            catch (Exception e)
            {
                scope.Failed(e);
                throw;
            }
        }

        /// <summary>
        /// [Protocol Method]
        /// <list type="bullet">
        /// <item>
        /// <description>
        /// This <see href="https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/core/Azure.Core/samples/ProtocolMethods.md">protocol method</see> allows explicit creation of the request and processing of the response for advanced scenarios.
        /// </description>
        /// </item>
        /// <item>
        /// <description>
        /// Please try the simpler <see cref="Create(TodoItem,IEnumerable{BinaryData},CancellationToken)"/> convenience overload with strongly typed models first.
        /// </description>
        /// </item>
        /// </list>
        /// </summary>
        /// <param name="content"> The content to send as the body of the request. </param>
        /// <param name="context"> The request context, which can override default behaviors of the client pipeline on a per-call basis. </param>
        /// <exception cref="ArgumentNullException"> <paramref name="content"/> is null. </exception>
        /// <exception cref="MessageFailedException"> Service returned a non-success status code. </exception>
        /// <returns> The response returned from the service. </returns>
        public virtual Result Create(RequestBody content, RequestOptions context = null)
        {
            Argument.AssertNotNull(content, nameof(content));

            using var scope = ClientDiagnostics.CreateSpan("TodoItems.Create");
            scope.Start();
            try
            {
                using PipelineMessage message = CreateCreateRequest(content, context);
                return Result.FromResponse(_pipeline.ProcessMessage(message, context));
            }
            catch (Exception e)
            {
                scope.Failed(e);
                throw;
            }
        }

        /// <param name="id"> The <see cref="long"/> to use. </param>
        /// <param name="cancellationToken"> The cancellation token to use. </param>
        public virtual async Task<Result<TodoItem>> GetTodoItemAsync(long id, CancellationToken cancellationToken = default)
        {
            RequestOptions context = FromCancellationToken(cancellationToken);
            Result result = await GetTodoItemAsync(id, context).ConfigureAwait(false);
            return Result.FromValue(TodoItem.FromResponse(result.GetRawResponse()), result.GetRawResponse());
        }

        /// <param name="id"> The <see cref="long"/> to use. </param>
        /// <param name="cancellationToken"> The cancellation token to use. </param>
        public virtual Result<TodoItem> GetTodoItem(long id, CancellationToken cancellationToken = default)
        {
            RequestOptions context = FromCancellationToken(cancellationToken);
            Result result = GetTodoItem(id, context);
            return Result.FromValue(TodoItem.FromResponse(result.GetRawResponse()), result.GetRawResponse());
        }

        /// <summary>
        /// [Protocol Method]
        /// <list type="bullet">
        /// <item>
        /// <description>
        /// This <see href="https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/core/Azure.Core/samples/ProtocolMethods.md">protocol method</see> allows explicit creation of the request and processing of the response for advanced scenarios.
        /// </description>
        /// </item>
        /// <item>
        /// <description>
        /// Please try the simpler <see cref="GetTodoItemAsync(long,CancellationToken)"/> convenience overload with strongly typed models first.
        /// </description>
        /// </item>
        /// </list>
        /// </summary>
        /// <param name="id"> The <see cref="long"/> to use. </param>
        /// <param name="context"> The request context, which can override default behaviors of the client pipeline on a per-call basis. </param>
        /// <exception cref="MessageFailedException"> Service returned a non-success status code. </exception>
        /// <returns> The response returned from the service. </returns>
        public virtual async Task<Result> GetTodoItemAsync(long id, RequestOptions context)
        {
            using var scope = ClientDiagnostics.CreateSpan("TodoItems.GetTodoItem");
            scope.Start();
            try
            {
                using PipelineMessage message = CreateGetTodoItemRequest(id, context);
                return Result.FromResponse(await _pipeline.ProcessMessageAsync(message, context).ConfigureAwait(false));
            }
            catch (Exception e)
            {
                scope.Failed(e);
                throw;
            }
        }

        /// <summary>
        /// [Protocol Method]
        /// <list type="bullet">
        /// <item>
        /// <description>
        /// This <see href="https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/core/Azure.Core/samples/ProtocolMethods.md">protocol method</see> allows explicit creation of the request and processing of the response for advanced scenarios.
        /// </description>
        /// </item>
        /// <item>
        /// <description>
        /// Please try the simpler <see cref="GetTodoItem(long,CancellationToken)"/> convenience overload with strongly typed models first.
        /// </description>
        /// </item>
        /// </list>
        /// </summary>
        /// <param name="id"> The <see cref="long"/> to use. </param>
        /// <param name="context"> The request context, which can override default behaviors of the client pipeline on a per-call basis. </param>
        /// <exception cref="MessageFailedException"> Service returned a non-success status code. </exception>
        /// <returns> The response returned from the service. </returns>
        public virtual Result GetTodoItem(long id, RequestOptions context)
        {
            using var scope = ClientDiagnostics.CreateSpan("TodoItems.GetTodoItem");
            scope.Start();
            try
            {
                using PipelineMessage message = CreateGetTodoItemRequest(id, context);
                return Result.FromResponse(_pipeline.ProcessMessage(message, context));
            }
            catch (Exception e)
            {
                scope.Failed(e);
                throw;
            }
        }

        /// <summary>
        /// [Protocol Method]
        /// <list type="bullet">
        /// <item>
        /// <description>
        /// This <see href="https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/core/Azure.Core/samples/ProtocolMethods.md">protocol method</see> allows explicit creation of the request and processing of the response for advanced scenarios.
        /// </description>
        /// </item>
        /// </list>
        /// </summary>
        /// <param name="id"> The <see cref="long"/> to use. </param>
        /// <param name="content"> The content to send as the body of the request. </param>
        /// <param name="context"> The request context, which can override default behaviors of the client pipeline on a per-call basis. </param>
        /// <exception cref="ArgumentNullException"> <paramref name="content"/> is null. </exception>
        /// <exception cref="MessageFailedException"> Service returned a non-success status code. </exception>
        /// <returns> The response returned from the service. </returns>
        public virtual async Task<Result> UpdateAsync(long id, RequestBody content, RequestOptions context = null)
        {
            Argument.AssertNotNull(content, nameof(content));

            using var scope = ClientDiagnostics.CreateSpan("TodoItems.Update");
            scope.Start();
            try
            {
                using PipelineMessage message = CreateUpdateRequest(id, content, context);
                return Result.FromResponse(await _pipeline.ProcessMessageAsync(message, context).ConfigureAwait(false));
            }
            catch (Exception e)
            {
                scope.Failed(e);
                throw;
            }
        }

        /// <summary>
        /// [Protocol Method]
        /// <list type="bullet">
        /// <item>
        /// <description>
        /// This <see href="https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/core/Azure.Core/samples/ProtocolMethods.md">protocol method</see> allows explicit creation of the request and processing of the response for advanced scenarios.
        /// </description>
        /// </item>
        /// </list>
        /// </summary>
        /// <param name="id"> The <see cref="long"/> to use. </param>
        /// <param name="content"> The content to send as the body of the request. </param>
        /// <param name="context"> The request context, which can override default behaviors of the client pipeline on a per-call basis. </param>
        /// <exception cref="ArgumentNullException"> <paramref name="content"/> is null. </exception>
        /// <exception cref="MessageFailedException"> Service returned a non-success status code. </exception>
        /// <returns> The response returned from the service. </returns>
        public virtual Result Update(long id, RequestBody content, RequestOptions context = null)
        {
            Argument.AssertNotNull(content, nameof(content));

            using var scope = ClientDiagnostics.CreateSpan("TodoItems.Update");
            scope.Start();
            try
            {
                using PipelineMessage message = CreateUpdateRequest(id, content, context);
                return Result.FromResponse(_pipeline.ProcessMessage(message, context));
            }
            catch (Exception e)
            {
                scope.Failed(e);
                throw;
            }
        }

        // The convenience method is omitted here because it has exactly the same parameter list as the corresponding protocol method
        /// <summary>
        /// [Protocol Method]
        /// <list type="bullet">
        /// <item>
        /// <description>
        /// This <see href="https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/core/Azure.Core/samples/ProtocolMethods.md">protocol method</see> allows explicit creation of the request and processing of the response for advanced scenarios.
        /// </description>
        /// </item>
        /// </list>
        /// </summary>
        /// <param name="id"> The <see cref="long"/> to use. </param>
        /// <param name="context"> The request context, which can override default behaviors of the client pipeline on a per-call basis. </param>
        /// <exception cref="MessageFailedException"> Service returned a non-success status code. </exception>
        /// <returns> The response returned from the service. </returns>
        public virtual async Task<Result> DeleteAsync(long id, RequestOptions context = null)
        {
            using var scope = ClientDiagnostics.CreateSpan("TodoItems.Delete");
            scope.Start();
            try
            {
                using PipelineMessage message = CreateDeleteRequest(id, context);
                return Result.FromResponse(await _pipeline.ProcessMessageAsync(message, context).ConfigureAwait(false));
            }
            catch (Exception e)
            {
                scope.Failed(e);
                throw;
            }
        }

        // The convenience method is omitted here because it has exactly the same parameter list as the corresponding protocol method
        /// <summary>
        /// [Protocol Method]
        /// <list type="bullet">
        /// <item>
        /// <description>
        /// This <see href="https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/core/Azure.Core/samples/ProtocolMethods.md">protocol method</see> allows explicit creation of the request and processing of the response for advanced scenarios.
        /// </description>
        /// </item>
        /// </list>
        /// </summary>
        /// <param name="id"> The <see cref="long"/> to use. </param>
        /// <param name="context"> The request context, which can override default behaviors of the client pipeline on a per-call basis. </param>
        /// <exception cref="MessageFailedException"> Service returned a non-success status code. </exception>
        /// <returns> The response returned from the service. </returns>
        public virtual Result Delete(long id, RequestOptions context = null)
        {
            using var scope = ClientDiagnostics.CreateSpan("TodoItems.Delete");
            scope.Start();
            try
            {
                using PipelineMessage message = CreateDeleteRequest(id, context);
                return Result.FromResponse(_pipeline.ProcessMessage(message, context));
            }
            catch (Exception e)
            {
                scope.Failed(e);
                throw;
            }
        }

        private TodoItemsAttachments _cachedTodoItemsAttachments;

        /// <summary> Initializes a new instance of TodoItemsAttachments. </summary>
        public virtual TodoItemsAttachments GetItemsAttachmentsClient()
        {
            return Volatile.Read(ref _cachedTodoItemsAttachments) ?? Interlocked.CompareExchange(ref _cachedTodoItemsAttachments, new TodoItemsAttachments(ClientDiagnostics, _pipeline, _keyCredential), null) ?? _cachedTodoItemsAttachments;
        }

        internal PipelineMessage CreateGetTodoItemsRequest(int? limit, int? offset, RequestOptions context)
        {
            var message = _pipeline.CreateMessage(context, ResponseErrorClassifier200);
            var request = message.Request;
            request.SetMethod("GET");
            var uri = new RequestUri();
            uri.AppendPath("/items", false);
            if (limit != null)
            {
                uri.AppendQuery("limit", limit.Value, true);
            }
            if (offset != null)
            {
                uri.AppendQuery("offset", offset.Value, true);
            }
            request.Uri = uri.ToUri();
            request.SetHeaderValue("Accept", "application/json");
            return message;
        }

        internal PipelineMessage CreateCreateRequest(RequestBody content, RequestOptions context)
        {
            var message = _pipeline.CreateMessage(context, ResponseErrorClassifier200);
            var request = message.Request;
            request.SetMethod("POST");
            var uri = new RequestUri();
            uri.AppendPath("/items", false);
            request.Uri = uri.ToUri();
            request.SetHeaderValue("Accept", "application/json");
            request.SetHeaderValue("content-type", "application/json");
            request.Content = content;
            return message;
        }

        internal PipelineMessage CreateGetTodoItemRequest(long id, RequestOptions context)
        {
            var message = _pipeline.CreateMessage(context, ResponseErrorClassifier200404);
            var request = message.Request;
            request.SetMethod("GET");
            var uri = new RequestUri();
            uri.AppendPath("/items/", false);
            uri.AppendPath(id.ToString(), true);
            request.Uri = uri.ToUri();
            request.SetHeaderValue("Accept", "application/json");
            return message;
        }

        internal PipelineMessage CreateUpdateRequest(long id, RequestBody content, RequestOptions context)
        {
            var message = _pipeline.CreateMessage(context, ResponseErrorClassifier200);
            var request = message.Request;
            request.SetMethod("PATCH");
            var uri = new RequestUri();
            uri.AppendPath("/items/", false);
            uri.AppendPath(id.ToString(), true);
            request.Uri = uri.ToUri();
            request.SetHeaderValue("Accept", "application/json");
            request.SetHeaderValue("content-type", "application/merge-patch+json");
            request.Content = content;
            return message;
        }

        internal PipelineMessage CreateDeleteRequest(long id, RequestOptions context)
        {
            var message = _pipeline.CreateMessage(context, ResponseErrorClassifier204404);
            var request = message.Request;
            request.SetMethod("DELETE");
            var uri = new RequestUri();
            uri.AppendPath("/items/", false);
            uri.AppendPath(id.ToString(), true);
            request.Uri = uri.ToUri();
            request.SetHeaderValue("Accept", "application/json");
            return message;
        }

        private static RequestOptions DefaultRequestContext = new RequestOptions();
        internal static RequestOptions FromCancellationToken(CancellationToken cancellationToken = default)
        {
            if (!cancellationToken.CanBeCanceled)
            {
                return DefaultRequestContext;
            }

            return new RequestOptions() { CancellationToken = cancellationToken };
        }

        private static ResponseErrorClassifier _responseErrorClassifier200;
        private static ResponseErrorClassifier ResponseErrorClassifier200 => _responseErrorClassifier200 ??= new StatusResponseClassifier(stackalloc ushort[] { 200 });
        private static ResponseErrorClassifier _responseErrorClassifier200404;
        private static ResponseErrorClassifier ResponseErrorClassifier200404 => _responseErrorClassifier200404 ??= new StatusResponseClassifier(stackalloc ushort[] { 200, 404 });
        private static ResponseErrorClassifier _responseErrorClassifier204404;
        private static ResponseErrorClassifier ResponseErrorClassifier204404 => _responseErrorClassifier204404 ??= new StatusResponseClassifier(stackalloc ushort[] { 204, 404 });
    }
}
