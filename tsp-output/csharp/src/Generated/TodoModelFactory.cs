// <auto-generated/>

#nullable disable

using System;
using System.Collections.Generic;
using System.Linq;

namespace Todo.Models
{
    /// <summary> Model factory for models. </summary>
    public static partial class TodoModelFactory
    {
        /// <summary> Initializes a new instance of <see cref="Models.User"/>. </summary>
        /// <param name="id"> An autogenerated unique id for the user. </param>
        /// <param name="username"> The user's username. </param>
        /// <param name="email"> The user's email address. </param>
        /// <param name="password">
        /// The user's password, provided when creating a user
        /// but is otherwise not visible (and hashed by the backend)
        /// </param>
        /// <param name="validated"> Whether the user is validated. Never visible to the API. </param>
        /// <returns> A new <see cref="Models.User"/> instance for mocking. </returns>
        public static User User(long id = default, string username = null, string email = null, string password = null, bool validated = default)
        {
            return new User(
                id,
                username,
                email,
                password,
                validated,
                serializedAdditionalRawData: null);
        }

        /// <summary> Initializes a new instance of <see cref="Models.UserCreatedResponse"/>. </summary>
        /// <param name="id"> An autogenerated unique id for the user. </param>
        /// <param name="username"> The user's username. </param>
        /// <param name="email"> The user's email address. </param>
        /// <param name="password">
        /// The user's password, provided when creating a user
        /// but is otherwise not visible (and hashed by the backend)
        /// </param>
        /// <param name="validated"> Whether the user is validated. Never visible to the API. </param>
        /// <param name="token"> The token to use to construct the validate email address url. </param>
        /// <returns> A new <see cref="Models.UserCreatedResponse"/> instance for mocking. </returns>
        public static UserCreatedResponse UserCreatedResponse(long id = default, string username = null, string email = null, string password = null, bool validated = default, string token = null)
        {
            return new UserCreatedResponse(
                id,
                username,
                email,
                password,
                validated,
                token,
                serializedAdditionalRawData: null);
        }

        /// <summary> Initializes a new instance of <see cref="Models.TodoPage"/>. </summary>
        /// <param name="items"> The items in the page. </param>
        /// <param name="pagination"></param>
        /// <returns> A new <see cref="Models.TodoPage"/> instance for mocking. </returns>
        public static TodoPage TodoPage(IEnumerable<TodoItem> items = null, TodoPagePagination pagination = null)
        {
            items ??= new List<TodoItem>();

            return new TodoPage(items?.ToList(), pagination, serializedAdditionalRawData: null);
        }

        /// <summary> Initializes a new instance of <see cref="Models.TodoItem"/>. </summary>
        /// <param name="id"> The item's unique id. </param>
        /// <param name="title"> The item's title. </param>
        /// <param name="createdBy"> User that created the todo. </param>
        /// <param name="assignedTo"> User that the todo is assigned to. </param>
        /// <param name="description"> A longer description of the todo item in markdown format. </param>
        /// <param name="status"> The status of the todo item. </param>
        /// <param name="createdAt"> When the todo item was created. </param>
        /// <param name="updatedAt"> When the todo item was last updated. </param>
        /// <param name="completedAt"> When the todo item was makred as completed. </param>
        /// <param name="labels"></param>
        /// <param name="dummy"></param>
        /// <returns> A new <see cref="Models.TodoItem"/> instance for mocking. </returns>
        public static TodoItem TodoItem(long id = default, string title = null, long createdBy = default, long? assignedTo = null, string description = null, TodoItemStatus status = default, DateTimeOffset createdAt = default, DateTimeOffset updatedAt = default, DateTimeOffset? completedAt = null, BinaryData labels = null, string dummy = null)
        {
            return new TodoItem(
                id,
                title,
                createdBy,
                assignedTo,
                description,
                status,
                createdAt,
                updatedAt,
                completedAt,
                labels,
                dummy,
                serializedAdditionalRawData: null);
        }

        /// <summary> Initializes a new instance of <see cref="Models.TodoPagePagination"/>. </summary>
        /// <param name="pageSize"> The number of items returned in this page. </param>
        /// <param name="totalSize"> The total number of items. </param>
        /// <param name="prevLink"> A link to the previous page, if it exists. </param>
        /// <param name="nextLink"> A link to the next page, if it exists. </param>
        /// <returns> A new <see cref="Models.TodoPagePagination"/> instance for mocking. </returns>
        public static TodoPagePagination TodoPagePagination(int pageSize = default, int totalSize = default, Uri prevLink = null, Uri nextLink = null)
        {
            return new TodoPagePagination(pageSize, totalSize, prevLink, nextLink, serializedAdditionalRawData: null);
        }
    }
}
