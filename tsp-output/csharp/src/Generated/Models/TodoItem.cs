// <auto-generated/>

#nullable disable

using System;
using System.Collections.Generic;
using Todo;

namespace Todo.Models
{
    /// <summary> The TodoItem. </summary>
    public partial class TodoItem
    {
        /// <summary>
        /// Keeps track of any properties unknown to the library.
        /// <para>
        /// To assign an object to the value of this property use <see cref="BinaryData.FromObjectAsJson{T}(T, System.Text.Json.JsonSerializerOptions?)"/>.
        /// </para>
        /// <para>
        /// To assign an already formatted json string to this property use <see cref="BinaryData.FromString(string)"/>.
        /// </para>
        /// <para>
        /// Examples:
        /// <list type="bullet">
        /// <item>
        /// <term>BinaryData.FromObjectAsJson("foo")</term>
        /// <description>Creates a payload of "foo".</description>
        /// </item>
        /// <item>
        /// <term>BinaryData.FromString("\"foo\"")</term>
        /// <description>Creates a payload of "foo".</description>
        /// </item>
        /// <item>
        /// <term>BinaryData.FromObjectAsJson(new { key = "value" })</term>
        /// <description>Creates a payload of { "key": "value" }.</description>
        /// </item>
        /// <item>
        /// <term>BinaryData.FromString("{\"key\": \"value\"}")</term>
        /// <description>Creates a payload of { "key": "value" }.</description>
        /// </item>
        /// </list>
        /// </para>
        /// </summary>
        private IDictionary<string, BinaryData> _serializedAdditionalRawData;

        /// <summary> Initializes a new instance of <see cref="TodoItem"/>. </summary>
        /// <param name="title"> The item's title. </param>
        /// <param name="status"> The status of the todo item. </param>
        /// <exception cref="ArgumentNullException"> <paramref name="title"/> is null. </exception>
        public TodoItem(string title, TodoItemStatus status)
        {
            Argument.AssertNotNull(title, nameof(title));

            Title = title;
            Status = status;
        }

        /// <summary> Initializes a new instance of <see cref="TodoItem"/>. </summary>
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
        /// <param name="serializedAdditionalRawData"> Keeps track of any properties unknown to the library. </param>
        internal TodoItem(long id, string title, long createdBy, long? assignedTo, string description, TodoItemStatus status, DateTimeOffset createdAt, DateTimeOffset updatedAt, DateTimeOffset? completedAt, BinaryData labels, string dummy, IDictionary<string, BinaryData> serializedAdditionalRawData)
        {
            Id = id;
            Title = title;
            CreatedBy = createdBy;
            AssignedTo = assignedTo;
            Description = description;
            Status = status;
            CreatedAt = createdAt;
            UpdatedAt = updatedAt;
            CompletedAt = completedAt;
            Labels = labels;
            Dummy = dummy;
            _serializedAdditionalRawData = serializedAdditionalRawData;
        }

        /// <summary> Initializes a new instance of <see cref="TodoItem"/> for deserialization. </summary>
        internal TodoItem()
        {
        }

        /// <summary> The item's unique id. </summary>
        public long Id { get; }
        /// <summary> The item's title. </summary>
        public string Title { get; set; }
        /// <summary> User that created the todo. </summary>
        public long CreatedBy { get; }
        /// <summary> User that the todo is assigned to. </summary>
        public long? AssignedTo { get; set; }
        /// <summary> A longer description of the todo item in markdown format. </summary>
        public string Description { get; set; }
        /// <summary> The status of the todo item. </summary>
        public TodoItemStatus Status { get; set; }
        /// <summary> When the todo item was created. </summary>
        public DateTimeOffset CreatedAt { get; }
        /// <summary> When the todo item was last updated. </summary>
        public DateTimeOffset UpdatedAt { get; }
        /// <summary> When the todo item was makred as completed. </summary>
        public DateTimeOffset? CompletedAt { get; }
        /// <summary>
        /// Gets or sets the labels
        /// <para>
        /// To assign an object to this property use <see cref="BinaryData.FromObjectAsJson{T}(T, System.Text.Json.JsonSerializerOptions?)"/>.
        /// </para>
        /// <para>
        /// To assign an already formatted json string to this property use <see cref="BinaryData.FromString(string)"/>.
        /// </para>
        /// <para>
        /// <remarks>
        /// Supported types:
        /// <list type="bullet">
        /// <item>
        /// <description><see cref="string"/></description>
        /// </item>
        /// <item>
        /// <description><see cref="IList{T}"/> where <c>T</c> is of type <see cref="string"/></description>
        /// </item>
        /// <item>
        /// <description><see cref="TodoLabelRecord"/></description>
        /// </item>
        /// <item>
        /// <description><see cref="IList{T}"/> where <c>T</c> is of type <see cref="TodoLabelRecord"/></description>
        /// </item>
        /// </list>
        /// </remarks>
        /// Examples:
        /// <list type="bullet">
        /// <item>
        /// <term>BinaryData.FromObjectAsJson("foo")</term>
        /// <description>Creates a payload of "foo".</description>
        /// </item>
        /// <item>
        /// <term>BinaryData.FromString("\"foo\"")</term>
        /// <description>Creates a payload of "foo".</description>
        /// </item>
        /// <item>
        /// <term>BinaryData.FromObjectAsJson(new { key = "value" })</term>
        /// <description>Creates a payload of { "key": "value" }.</description>
        /// </item>
        /// <item>
        /// <term>BinaryData.FromString("{\"key\": \"value\"}")</term>
        /// <description>Creates a payload of { "key": "value" }.</description>
        /// </item>
        /// </list>
        /// </para>
        /// </summary>
        public BinaryData Labels { get; set; }
        /// <summary> Gets or sets the dummy. </summary>
        public string Dummy { get; set; }
    }
}
