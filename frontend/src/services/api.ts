import ax from "./axios_instance";
import { z } from "zod";

const TimeSeriesDataSchema = z.array(
  z.object({
    time: z.number(),
    value: z.number(),
  })
);

export type TimeSeriesData = z.infer<typeof TimeSeriesDataSchema>;

export const getOverallSleepScore = async (): Promise<TimeSeriesData> => {
  const response = await ax.get<TimeSeriesData>("sleep/overall_score");
  return TimeSeriesDataSchema.parse(response.data);
};

export const getRevitalizationScore = async (): Promise<TimeSeriesData> => {
  const response = await ax.get<TimeSeriesData>("sleep/revitalization_score");
  return TimeSeriesDataSchema.parse(response.data);
};

export const getDeepSleepMinutes = async (): Promise<TimeSeriesData> => {
  const response = await ax.get<TimeSeriesData>("sleep/deep_sleep_minutes");
  return TimeSeriesDataSchema.parse(response.data);
};

export const getRestingHeartRate = async (): Promise<TimeSeriesData> => {
  const response = await ax.get<TimeSeriesData>("sleep/rhr");
  return TimeSeriesDataSchema.parse(response.data);
};

export const getRestlessness = async (): Promise<TimeSeriesData> => {
  const response = await ax.get<TimeSeriesData>("sleep/restlessness");
  return TimeSeriesDataSchema.parse(response.data);
};
