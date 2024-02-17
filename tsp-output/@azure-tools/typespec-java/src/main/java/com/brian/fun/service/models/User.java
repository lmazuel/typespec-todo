// Code generated by Microsoft (R) TypeSpec Code Generator.

package com.brian.fun.service.models;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.generic.core.annotation.Generated;
import com.generic.core.annotation.Immutable;

/**
 * The User model.
 */
@Immutable
public final class User {
    /*
     * An autogenerated unique id for the user
     */
    @Generated
    @JsonProperty(value = "id", access = JsonProperty.Access.WRITE_ONLY)
    private long id;

    /*
     * The user's username
     */
    @Generated
    @JsonProperty(value = "username")
    private String username;

    /*
     * The user's email address
     */
    @Generated
    @JsonProperty(value = "email")
    private String email;

    /*
     * The user's password, provided when creating a user
     * but is otherwise not visible (and hashed by the backend)
     */
    @Generated
    @JsonProperty(value = "password")
    private String password;

    /**
     * Creates an instance of User class.
     * 
     * @param username the username value to set.
     * @param email the email value to set.
     * @param password the password value to set.
     */
    @Generated
    @JsonCreator
    public User(@JsonProperty(value = "username") String username, @JsonProperty(value = "email") String email,
        @JsonProperty(value = "password") String password) {
        this.username = username;
        this.email = email;
        this.password = password;
    }

    /**
     * Get the id property: An autogenerated unique id for the user.
     * 
     * @return the id value.
     */
    @Generated
    public long getId() {
        return this.id;
    }

    /**
     * Get the username property: The user's username.
     * 
     * @return the username value.
     */
    @Generated
    public String getUsername() {
        return this.username;
    }

    /**
     * Get the email property: The user's email address.
     * 
     * @return the email value.
     */
    @Generated
    public String getEmail() {
        return this.email;
    }

    /**
     * Get the password property: The user's password, provided when creating a user
     * but is otherwise not visible (and hashed by the backend).
     * 
     * @return the password value.
     */
    @Generated
    public String getPassword() {
        return this.password;
    }
}
