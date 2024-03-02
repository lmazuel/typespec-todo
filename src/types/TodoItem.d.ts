/* eslint-disable */
/**
 * This file was automatically generated by json-schema-to-typescript.
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSONSchema file,
 * and run json-schema-to-typescript to regenerate this file.
 */

export type TodoLabelsJson = string | string[] | TodoLabelRecordJson | TodoLabelRecordJson[];

export interface TodoItemJson {
  /**
   * The item's unique id
   */
  id: number;
  /**
   * The item's title
   */
  title: string;
  /**
   * User that created the todo
   */
  createdBy: number;
  /**
   * User that the todo is assigned to
   */
  assignedTo?: number;
  /**
   * A longer description of the todo item in markdown format
   */
  description?: string;
  /**
   * The status of the todo item
   */
  status: "NotStarted" | "InProgress" | "Completed";
  /**
   * When the todo item was created.
   */
  createdAt: string;
  /**
   * When the todo item was last updated
   */
  updatedAt: string;
  /**
   * When the todo item was makred as completed
   */
  completedAt?: string;
  labels?: TodoLabelsJson;
  _dummy?: string;
}
export interface TodoLabelRecordJson {
  name: string;
  color?: string;
}
