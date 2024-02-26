// Code generated by Microsoft (R) TypeSpec Code Generator.

package com.brian.fun.service;

import com.brian.fun.service.implementation.MultipartFormDataHelper;
import com.brian.fun.service.implementation.TodoItemsImpl;
import com.brian.fun.service.implementation.models.CreateFormRequest;
import com.brian.fun.service.implementation.models.CreateJsonRequest;
import com.brian.fun.service.models.TodoItem;
import com.brian.fun.service.models.TodoPage;
import com.generic.core.annotation.Generated;
import com.generic.core.annotation.ReturnType;
import com.generic.core.annotation.ServiceClient;
import com.generic.core.annotation.ServiceMethod;
import com.generic.core.exception.ClientAuthenticationException;
import com.generic.core.exception.HttpResponseException;
import com.generic.core.exception.ResourceModifiedException;
import com.generic.core.exception.ResourceNotFoundException;
import com.generic.core.http.Response;
import com.generic.core.models.BinaryData;
import com.generic.core.models.RequestOptions;
import java.util.List;

/**
 * Initializes a new instance of the synchronous TodoClient type.
 */
@ServiceClient(builder = TodoClientBuilder.class)
public final class TodoItemsClient {
    @Generated
    private final TodoItemsImpl serviceClient;

    /**
     * Initializes an instance of TodoItemsClient class.
     * 
     * @param serviceClient the service client implementation.
     */
    @Generated
    TodoItemsClient(TodoItemsImpl serviceClient) {
        this.serviceClient = serviceClient;
    }

    /**
     * The list operation.
     * <p>
     * <strong>Response Body Schema</strong>
     * </p>
     * <pre>{@code
     * {
     *     items (Required): [
     *          (Required){
     *             id: long (Required)
     *             title: String (Required)
     *             createdBy: long (Required)
     *             assignedTo: Long (Optional)
     *             description: String (Optional)
     *             status: String(NotStarted/InProgress/Completed) (Required)
     *             createdAt: OffsetDateTime (Required)
     *             updatedAt: OffsetDateTime (Required)
     *             completedAt: OffsetDateTime (Required)
     *             labels (Required): [
     *                 BinaryData (Required)
     *             ]
     *         }
     *     ]
     *     pagination (Required): {
     *         pageSize: int (Required)
     *         totalSize: int (Required)
     *         prevLink: String (Optional)
     *         nextLink: String (Optional)
     *     }
     * }
     * }</pre>
     * 
     * @param limit The limit to the number of items.
     * @param offset The offset to start paginating at.
     * @param requestOptions The options to configure the HTTP request before HTTP client sends it.
     * @throws HttpResponseException thrown if the request is rejected by server.
     * @throws ResourceModifiedException thrown if the request is rejected by server on status code 409.
     * @throws ResourceNotFoundException thrown if the request is rejected by server on status code 404.
     * @throws ClientAuthenticationException thrown if the request is rejected by server on status code 401.
     * @return the response.
     */
    @Generated
    @ServiceMethod(returns = ReturnType.SINGLE)
    public Response<BinaryData> listWithResponse(int limit, int offset, RequestOptions requestOptions) {
        return this.serviceClient.listWithResponse(limit, offset, requestOptions);
    }

    /**
     * The createJson operation.
     * <p>
     * <strong>Request Body Schema</strong>
     * </p>
     * <pre>{@code
     * {
     *     item (Required): {
     *         id: long (Required)
     *         title: String (Required)
     *         createdBy: long (Required)
     *         assignedTo: Long (Optional)
     *         description: String (Optional)
     *         status: String(NotStarted/InProgress/Completed) (Required)
     *         createdAt: OffsetDateTime (Required)
     *         updatedAt: OffsetDateTime (Required)
     *         completedAt: OffsetDateTime (Required)
     *         labels (Required): [
     *             BinaryData (Required)
     *         ]
     *     }
     *     attachments (Required): [
     *         BinaryData (Required)
     *     ]
     * }
     * }</pre>
     * <p>
     * <strong>Response Body Schema</strong>
     * </p>
     * <pre>{@code
     * {
     *     id: long (Required)
     *     title: String (Required)
     *     createdBy: long (Required)
     *     assignedTo: Long (Optional)
     *     description: String (Optional)
     *     status: String(NotStarted/InProgress/Completed) (Required)
     *     createdAt: OffsetDateTime (Required)
     *     updatedAt: OffsetDateTime (Required)
     *     completedAt: OffsetDateTime (Required)
     *     labels (Required): [
     *         BinaryData (Required)
     *     ]
     * }
     * }</pre>
     * 
     * @param request The request parameter.
     * @param requestOptions The options to configure the HTTP request before HTTP client sends it.
     * @throws HttpResponseException thrown if the request is rejected by server.
     * @throws ResourceModifiedException thrown if the request is rejected by server on status code 409.
     * @throws ResourceNotFoundException thrown if the request is rejected by server on status code 404.
     * @throws ClientAuthenticationException thrown if the request is rejected by server on status code 401.
     * @return the response.
     */
    @Generated
    @ServiceMethod(returns = ReturnType.SINGLE)
    public Response<BinaryData> createJsonWithResponse(BinaryData request, RequestOptions requestOptions) {
        return this.serviceClient.createJsonWithResponse(request, requestOptions);
    }

    /**
     * The createForm operation.
     * <p>
     * <strong>Response Body Schema</strong>
     * </p>
     * <pre>{@code
     * {
     *     id: long (Required)
     *     title: String (Required)
     *     createdBy: long (Required)
     *     assignedTo: Long (Optional)
     *     description: String (Optional)
     *     status: String(NotStarted/InProgress/Completed) (Required)
     *     createdAt: OffsetDateTime (Required)
     *     updatedAt: OffsetDateTime (Required)
     *     completedAt: OffsetDateTime (Required)
     *     labels (Required): [
     *         BinaryData (Required)
     *     ]
     * }
     * }</pre>
     * 
     * @param request The request parameter.
     * @param requestOptions The options to configure the HTTP request before HTTP client sends it.
     * @throws HttpResponseException thrown if the request is rejected by server.
     * @throws ResourceModifiedException thrown if the request is rejected by server on status code 409.
     * @throws ResourceNotFoundException thrown if the request is rejected by server on status code 404.
     * @throws ClientAuthenticationException thrown if the request is rejected by server on status code 401.
     * @return the response.
     */
    @Generated
    @ServiceMethod(returns = ReturnType.SINGLE)
    Response<BinaryData> createFormWithResponse(BinaryData request, RequestOptions requestOptions) {
        // Protocol API requires serialization of parts with content-disposition and data, as operation 'createForm' is
        // 'multipart/form-data'
        return this.serviceClient.createFormWithResponse(request, requestOptions);
    }

    /**
     * The get operation.
     * <p>
     * <strong>Response Body Schema</strong>
     * </p>
     * <pre>{@code
     * {
     *     id: long (Required)
     *     title: String (Required)
     *     createdBy: long (Required)
     *     assignedTo: Long (Optional)
     *     description: String (Optional)
     *     status: String(NotStarted/InProgress/Completed) (Required)
     *     createdAt: OffsetDateTime (Required)
     *     updatedAt: OffsetDateTime (Required)
     *     completedAt: OffsetDateTime (Required)
     *     labels (Required): [
     *         BinaryData (Required)
     *     ]
     * }
     * }</pre>
     * 
     * @param id An integer that can be serialized to JSON (`−9007199254740991 (−(2^53 − 1))` to `9007199254740991 (2^53
     * − 1)` ).
     * @param requestOptions The options to configure the HTTP request before HTTP client sends it.
     * @throws HttpResponseException thrown if the request is rejected by server.
     * @throws ResourceModifiedException thrown if the request is rejected by server on status code 409.
     * @throws ClientAuthenticationException thrown if the request is rejected by server on status code 401.
     * @return the response.
     */
    @Generated
    @ServiceMethod(returns = ReturnType.SINGLE)
    public Response<BinaryData> getWithResponse(long id, RequestOptions requestOptions) {
        return this.serviceClient.getWithResponse(id, requestOptions);
    }

    /**
     * The update operation.
     * <p>
     * <strong>Request Body Schema</strong>
     * </p>
     * <pre>{@code
     * {
     *     patch (Required): {
     *         title: String (Optional)
     *         assignedTo: Long (Optional)
     *         description: String (Optional)
     *         status: String(NotStarted/InProgress/Completed) (Optional)
     *     }
     * }
     * }</pre>
     * <p>
     * <strong>Response Body Schema</strong>
     * </p>
     * <pre>{@code
     * {
     *     id: long (Required)
     *     title: String (Required)
     *     createdBy: long (Required)
     *     assignedTo: Long (Optional)
     *     description: String (Optional)
     *     status: String(NotStarted/InProgress/Completed) (Required)
     *     createdAt: OffsetDateTime (Required)
     *     updatedAt: OffsetDateTime (Required)
     *     completedAt: OffsetDateTime (Required)
     *     labels (Required): [
     *         BinaryData (Required)
     *     ]
     * }
     * }</pre>
     * 
     * @param id An integer that can be serialized to JSON (`−9007199254740991 (−(2^53 − 1))` to `9007199254740991 (2^53
     * − 1)` ).
     * @param request The request parameter.
     * @param requestOptions The options to configure the HTTP request before HTTP client sends it.
     * @throws HttpResponseException thrown if the request is rejected by server.
     * @throws ResourceModifiedException thrown if the request is rejected by server on status code 409.
     * @throws ResourceNotFoundException thrown if the request is rejected by server on status code 404.
     * @throws ClientAuthenticationException thrown if the request is rejected by server on status code 401.
     * @return the response.
     */
    @Generated
    @ServiceMethod(returns = ReturnType.SINGLE)
    public Response<BinaryData> updateWithResponse(long id, BinaryData request, RequestOptions requestOptions) {
        // Convenience API is not generated, as operation 'update' is 'application/merge-patch+json' and
        // stream-style-serialization is not enabled
        return this.serviceClient.updateWithResponse(id, request, requestOptions);
    }

    /**
     * The delete operation.
     * 
     * @param id An integer that can be serialized to JSON (`−9007199254740991 (−(2^53 − 1))` to `9007199254740991 (2^53
     * − 1)` ).
     * @param requestOptions The options to configure the HTTP request before HTTP client sends it.
     * @throws HttpResponseException thrown if the request is rejected by server.
     * @throws ResourceModifiedException thrown if the request is rejected by server on status code 409.
     * @throws ClientAuthenticationException thrown if the request is rejected by server on status code 401.
     * @return the response.
     */
    @Generated
    @ServiceMethod(returns = ReturnType.SINGLE)
    public Response<Void> deleteWithResponse(long id, RequestOptions requestOptions) {
        return this.serviceClient.deleteWithResponse(id, requestOptions);
    }

    /**
     * The list operation.
     * 
     * @param limit The limit to the number of items.
     * @param offset The offset to start paginating at.
     * @throws IllegalArgumentException thrown if parameters fail the validation.
     * @throws HttpResponseException thrown if the request is rejected by server.
     * @throws ResourceModifiedException thrown if the request is rejected by server on status code 409.
     * @throws ResourceNotFoundException thrown if the request is rejected by server on status code 404.
     * @throws ClientAuthenticationException thrown if the request is rejected by server on status code 401.
     * @throws RuntimeException all other wrapped checked exceptions if the request fails to be sent.
     * @return the response.
     */
    @Generated
    @ServiceMethod(returns = ReturnType.SINGLE)
    public TodoPage list(int limit, int offset) {
        // Generated convenience method for listWithResponse
        RequestOptions requestOptions = new RequestOptions();
        return listWithResponse(limit, offset, requestOptions).getValue().toObject(TodoPage.class);
    }

    /**
     * The createJson operation.
     * 
     * @param item The item parameter.
     * @param attachments The attachments parameter.
     * @throws IllegalArgumentException thrown if parameters fail the validation.
     * @throws HttpResponseException thrown if the request is rejected by server.
     * @throws ResourceModifiedException thrown if the request is rejected by server on status code 409.
     * @throws ResourceNotFoundException thrown if the request is rejected by server on status code 404.
     * @throws ClientAuthenticationException thrown if the request is rejected by server on status code 401.
     * @throws RuntimeException all other wrapped checked exceptions if the request fails to be sent.
     * @return the response.
     */
    @Generated
    @ServiceMethod(returns = ReturnType.SINGLE)
    public TodoItem createJson(TodoItem item, List<BinaryData> attachments) {
        // Generated convenience method for createJsonWithResponse
        RequestOptions requestOptions = new RequestOptions();
        CreateJsonRequest requestObj = new CreateJsonRequest(item, attachments);
        BinaryData request = BinaryData.fromObject(requestObj);
        return createJsonWithResponse(request, requestOptions).getValue().toObject(TodoItem.class);
    }

    /**
     * The createForm operation.
     * 
     * @param item The item parameter.
     * @param attachments The attachments parameter.
     * @throws IllegalArgumentException thrown if parameters fail the validation.
     * @throws HttpResponseException thrown if the request is rejected by server.
     * @throws ResourceModifiedException thrown if the request is rejected by server on status code 409.
     * @throws ResourceNotFoundException thrown if the request is rejected by server on status code 404.
     * @throws ClientAuthenticationException thrown if the request is rejected by server on status code 401.
     * @throws RuntimeException all other wrapped checked exceptions if the request fails to be sent.
     * @return the response.
     */
    @Generated
    @ServiceMethod(returns = ReturnType.SINGLE)
    public TodoItem createForm(TodoItem item, List<BinaryData> attachments) {
        // Generated convenience method for createFormWithResponse
        RequestOptions requestOptions = new RequestOptions();
        CreateFormRequest requestObj = new CreateFormRequest(item).setAttachments(attachments);
        BinaryData request
            = new MultipartFormDataHelper(requestOptions).serializeJsonField("item", requestObj.getItem())
                .serializeJsonField("attachments", requestObj.getAttachments()).end().getRequestBody();
        return createFormWithResponse(request, requestOptions).getValue().toObject(TodoItem.class);
    }

    /**
     * The createForm operation.
     * 
     * @param item The item parameter.
     * @throws IllegalArgumentException thrown if parameters fail the validation.
     * @throws HttpResponseException thrown if the request is rejected by server.
     * @throws ResourceModifiedException thrown if the request is rejected by server on status code 409.
     * @throws ResourceNotFoundException thrown if the request is rejected by server on status code 404.
     * @throws ClientAuthenticationException thrown if the request is rejected by server on status code 401.
     * @throws RuntimeException all other wrapped checked exceptions if the request fails to be sent.
     * @return the response.
     */
    @Generated
    @ServiceMethod(returns = ReturnType.SINGLE)
    public TodoItem createForm(TodoItem item) {
        // Generated convenience method for createFormWithResponse
        RequestOptions requestOptions = new RequestOptions();
        CreateFormRequest requestObj = new CreateFormRequest(item);
        BinaryData request
            = new MultipartFormDataHelper(requestOptions).serializeJsonField("item", requestObj.getItem())
                .serializeJsonField("attachments", requestObj.getAttachments()).end().getRequestBody();
        return createFormWithResponse(request, requestOptions).getValue().toObject(TodoItem.class);
    }

    /**
     * The get operation.
     * 
     * @param id An integer that can be serialized to JSON (`−9007199254740991 (−(2^53 − 1))` to `9007199254740991 (2^53
     * − 1)` ).
     * @throws IllegalArgumentException thrown if parameters fail the validation.
     * @throws HttpResponseException thrown if the request is rejected by server.
     * @throws ResourceModifiedException thrown if the request is rejected by server on status code 409.
     * @throws ClientAuthenticationException thrown if the request is rejected by server on status code 401.
     * @throws RuntimeException all other wrapped checked exceptions if the request fails to be sent.
     * @return the response.
     */
    @Generated
    @ServiceMethod(returns = ReturnType.SINGLE)
    public TodoItem get(long id) {
        // Generated convenience method for getWithResponse
        RequestOptions requestOptions = new RequestOptions();
        return getWithResponse(id, requestOptions).getValue().toObject(TodoItem.class);
    }

    /**
     * The delete operation.
     * 
     * @param id An integer that can be serialized to JSON (`−9007199254740991 (−(2^53 − 1))` to `9007199254740991 (2^53
     * − 1)` ).
     * @throws IllegalArgumentException thrown if parameters fail the validation.
     * @throws HttpResponseException thrown if the request is rejected by server.
     * @throws ResourceModifiedException thrown if the request is rejected by server on status code 409.
     * @throws ClientAuthenticationException thrown if the request is rejected by server on status code 401.
     * @throws RuntimeException all other wrapped checked exceptions if the request fails to be sent.
     */
    @Generated
    @ServiceMethod(returns = ReturnType.SINGLE)
    public void delete(long id) {
        // Generated convenience method for deleteWithResponse
        RequestOptions requestOptions = new RequestOptions();
        deleteWithResponse(id, requestOptions).getValue();
    }
}
