import axios from "axios";
import * as AxiosLogger from "axios-logger";

const apiBaseUrl = "http://localhost:8000";

const ax = axios.create({
  baseURL: `${apiBaseUrl}/api/v1/`,
});

ax.interceptors.request.use(AxiosLogger.requestLogger, AxiosLogger.errorLogger);
ax.interceptors.response.use(
  AxiosLogger.responseLogger,
  AxiosLogger.errorLogger
);

export default ax;
