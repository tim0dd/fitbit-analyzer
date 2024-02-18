import { useEffect, useRef, useState } from "react";
import {
  createChart,
  IChartApi,
  LineData,
  UTCTimestamp,
} from "lightweight-charts";
import type { TimeSeriesData } from "../services/api";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Toggle } from "./ui/toggle";

interface TimeSeriesChartProps {
  data: TimeSeriesData;
  title: string;
}

const TimeSeriesChart = ({ data, title }: TimeSeriesChartProps) => {
  const chartContainerRef = useRef<HTMLDivElement>(null);
  const [chart, setChart] = useState<IChartApi | null>(null);
  const [lineSeries, setLineSeries] = useState<any>(null); // Assuming lineSeries type
  const [showEMA, setShowEMA] = useState(false);
  // Chart initialization
  useEffect(() => {
    if (chartContainerRef.current && !chart) {
      const newChart = createChart(chartContainerRef.current, {
        width: chartContainerRef.current.offsetWidth,
        height: 300,
      });
      const newLineSeries = newChart.addLineSeries();
      setChart(newChart);
      setLineSeries(newLineSeries);
      return () => {
        newChart.remove();
      };
    }
  }, []);

  // Update line series data
  useEffect(() => {
    if (lineSeries && data) {
      const lineData: LineData[] = data.map((d) => ({
        value: d.value,
        time: d.time as UTCTimestamp,
      }));

      lineSeries.setData(lineData);
    }
  }, [data, lineSeries]);

  useEffect(() => {
    if (lineSeries) {
      const chartData = showEMA ? calculateEMA(data) : convertToLineData(data);
      lineSeries.setData(chartData);
    }
  }, [data, lineSeries, showEMA]);

  const calculateEMA = (data: TimeSeriesData, period = 10) => {
    if (data.length < period) {
      throw new Error(
        "Data length must be greater than or equal to the period."
      );
    }

    const k = 2 / (period + 1);
    let emaData: TimeSeriesData = [];

    // Calculate the initial SMA for the first EMA value
    let sma =
      data.slice(0, period).reduce((sum, curr) => sum + curr.value, 0) / period;
    emaData.push({ time: data[period - 1].time, value: sma });

    // Calculate the rest of the EMA values
    for (let i = period; i < data.length; i++) {
      const emaValue =
        data[i].value * k + emaData[emaData.length - 1].value * (1 - k);
      emaData.push({ time: data[i].time, value: emaValue });
    }

    return emaData;
  };

  const convertToLineData = (data: TimeSeriesData): LineData[] => {
    return data.map((d) => ({
      value: d.value,
      time: d.time as UTCTimestamp,
    }));
  };

  const toggleEMA = () => {
    setShowEMA(!showEMA);
  };

  return (
    <Card className="max-w-full md:max-w-2xl mx-auto">
      <CardHeader>
        <CardTitle>{title}</CardTitle>
      </CardHeader>
      <CardContent className="p-2">
        <Toggle pressed={showEMA} onPressedChange={toggleEMA} className="mb-3">
          {showEMA ? "EMA" : "EMA"}
        </Toggle>
        <div
          ref={chartContainerRef}
          className="w-full h-72 shadow-md rounded-lg"
        />
      </CardContent>
    </Card>
  );
};

export default TimeSeriesChart;
