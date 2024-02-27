// Copyright (c) Microsoft Corporation.
// Licensed under the MIT license.

import { getClient, ClientOptions } from "@azure-rest/core-client";
import { logger } from "./logger";
import { KeyCredential } from "@azure/core-auth";
import { BrianFunServiceClient } from "./clientDefinitions";

/**
 * Initialize a new instance of `BrianFunServiceClient`
 * @param endpoint - The parameter endpoint
 * @param credentials - uniquely identify client credential
 * @param options - the parameter for all optional parameters
 */
export default function createClient(
  endpoint: string,
  credentials: KeyCredential,
  options: ClientOptions = {},
): BrianFunServiceClient {
  const baseUrl = options.baseUrl ?? `${endpoint}`;

  const userAgentInfo = `azsdk-js-brian-fun-service-rest/1.0.0-beta.1`;
  const userAgentPrefix =
    options.userAgentOptions && options.userAgentOptions.userAgentPrefix
      ? `${options.userAgentOptions.userAgentPrefix} ${userAgentInfo}`
      : `${userAgentInfo}`;
  options = {
    ...options,
    userAgentOptions: {
      userAgentPrefix,
    },
    loggingOptions: {
      logger: options.loggingOptions?.logger ?? logger.info,
    },
  };

  const client = getClient(baseUrl, options) as BrianFunServiceClient;

  client.pipeline.removePolicy({ name: "ApiVersionPolicy" });

  client.pipeline.addPolicy({
    name: "customKeyCredentialPolicy",
    async sendRequest(request, next) {
      request.headers.set("Authorization", "bearer " + credentials.key);
      return next(request);
    },
  });
  return client;
}
