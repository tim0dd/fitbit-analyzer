import React, { useState, useEffect } from 'react';
import TimeSeriesChart from '../components/TimeSeriesChart';
import { TimeSeriesData, getOverallSleepScore, getRevitalizationScore, getDeepSleepMinutes, getRestingHeartRate, getRestlessness } from '../services/api';

interface ChartData {
    title: string;
    data: TimeSeriesData;
    loading: boolean;
}

const initialChartData: ChartData = { title: '', data: [], loading: true };

const DashboardPage = () => {
    const [overallSleepScore, setOverallSleepScore] = useState<ChartData>({ ...initialChartData, title: 'Overall Sleep Score' });
    const [revitalizationScore, setRevitalizationScore] = useState<ChartData>({ ...initialChartData, title: 'Revitalization Score' });
    const [deepSleepMinutes, setDeepSleepMinutes] = useState<ChartData>({ ...initialChartData, title: 'Deep Sleep Minutes' });
    const [restingHeartRate, setRestingHeartRate] = useState<ChartData>({ ...initialChartData, title: 'Resting Heart Rate' });
    const [restlessness, setRestlessness] = useState<ChartData>({ ...initialChartData, title: 'Restlessness' });

    useEffect(() => {
        const fetchData = async () => {
            try {
                const fetchedOverallSleepScore = await getOverallSleepScore();
                setOverallSleepScore({ ...overallSleepScore, data: fetchedOverallSleepScore, loading: false });

                const fetchedRevitalizationScore = await getRevitalizationScore();
                setRevitalizationScore({ ...revitalizationScore, data: fetchedRevitalizationScore, loading: false });

                const fetchedDeepSleepMinutes = await getDeepSleepMinutes();
                setDeepSleepMinutes({ ...deepSleepMinutes, data: fetchedDeepSleepMinutes, loading: false });

                const fetchedRestingHeartRate = await getRestingHeartRate();
                setRestingHeartRate({ ...restingHeartRate, data: fetchedRestingHeartRate, loading: false });

                const fetchedRestlessness = await getRestlessness();
                setRestlessness({ ...restlessness, data: fetchedRestlessness, loading: false });
            } catch (error) {
                console.error('Error fetching time series data:', error);
            }
        };

        fetchData();
    }, []);

    const charts = [overallSleepScore, revitalizationScore, deepSleepMinutes, restingHeartRate, restlessness];

    return (
        <div>
            {charts.map((chart, index) => (
                <div key={index}>
                    {chart.loading ? (
                        <p>Loading {chart.title}...</p>
                    ) : (
                        <TimeSeriesChart title={chart.title} data={chart.data} />
                    )}
                </div>
            ))}
        </div>
    );
};

export default DashboardPage;
