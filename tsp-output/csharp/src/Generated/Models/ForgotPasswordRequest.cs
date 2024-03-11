// <auto-generated/>

#nullable disable

using System;
using System.Collections.Generic;
using Todo;

namespace Todo.Models
{
    /// <summary> The ForgotPasswordRequest. </summary>
    internal partial class ForgotPasswordRequest
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

        /// <summary> Initializes a new instance of <see cref="ForgotPasswordRequest"/>. </summary>
        /// <param name="email"></param>
        /// <exception cref="ArgumentNullException"> <paramref name="email"/> is null. </exception>
        public ForgotPasswordRequest(string email)
        {
            Argument.AssertNotNull(email, nameof(email));

            Email = email;
        }

        /// <summary> Initializes a new instance of <see cref="ForgotPasswordRequest"/>. </summary>
        /// <param name="email"></param>
        /// <param name="serializedAdditionalRawData"> Keeps track of any properties unknown to the library. </param>
        internal ForgotPasswordRequest(string email, IDictionary<string, BinaryData> serializedAdditionalRawData)
        {
            Email = email;
            _serializedAdditionalRawData = serializedAdditionalRawData;
        }

        /// <summary> Initializes a new instance of <see cref="ForgotPasswordRequest"/> for deserialization. </summary>
        internal ForgotPasswordRequest()
        {
        }

        /// <summary> Gets the email. </summary>
        public string Email { get; }
    }
}
