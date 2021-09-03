import React, {useState, useEffect} from 'react';
import {StyleSheet, Text, View} from 'react-native';

import {
  VictoryLine,
  VictoryChart,
  VictoryTheme,
  VictoryZoomContainer,
  VictoryTooltip,
  VictoryBrushContainer,
  VictoryVoronoiContainer,
  VictoryAxis,
  createContainer,
} from 'victory-native';
import {NavigationContainer} from '@react-navigation/native';
import * as co2data from './co2data.json';

export default function charts({navigation}) {
  const VictoryZoomVoronoiContainer = createContainer('zoom', 'voronoi');

  const [selectedDomain, setSelectedDomain] = useState();
  const [zoomDomain, setZoomDomain] = useState();

  const handleZoom = domain => {
    setSelectedDomain(domain);
  };
  const handleBrush = domain => {
    setZoomDomain(domain);
  };

  const sensorData = co2data['default'];

  return (
    <>
      <View style={styles.container}>
        <Text style={styles.heading}>Room Lobby:100 - Raspberry1</Text>

        <VictoryChart
          domain={{y: [0, 800]}}
          theme={VictoryTheme.material}
          width={370}
          height={700}
          padding={{top: 40, left: 60, right: 5, bottom: 100}}
          domainPadding={20}
          containerComponent={
            <VictoryZoomVoronoiContainer
              zoomDimension="x"
              zoomDomain={zoomDomain}
              onZoomDomainChange={handleZoom}
              labels={({datum}) => `co2:${datum.co2}`}
            />
          }>
          <VictoryAxis
            dependentAxis
            fixLabelOverlap={true}
            label="Co2 in ppm"
            style={{
              axisLabel: {
                padding: 35,
                fontSize: 15,
                fontWeight: 'bold',
                fill: 'blue',
              },
              axis: {stroke: 'black'},
              ticks: {stroke: 'black', size: 5},
              tickLabels: {
                fill: 'black', //CHANGE COLOR OF Y-AXIS LABELS
                fontWeight: 'bold',
                fontSize: 12,
              },
            }}
          />
          <VictoryAxis
            independentAxis
            fixLabelOverlap={true}
            label="DateTime Interval"
            style={{
              axisLabel: {
                padding: 40,
                fontSize: 15,
                fontWeight: 'bold',
                fill: 'blue',
              },
              axis: {stroke: 'black'},
              ticks: {stroke: 'black', size: 5},
              tickLabels: {
                fill: 'black', //CHANGE COLOR OF X-AXIS LABELS
                fontWeight: 'bold',
                fontSize: 12,
              },
            }}
          />

          <VictoryLine
            style={{
              data: {stroke: '#00b300', strokeWidth: 3},
              parent: {border: '1px solid #ccc'},
            }}
            interpolation="catmullRom"
            data={sensorData}
            x="Time"
            y="co2"
          />
        </VictoryChart>
      </View>
    </>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,

    paddingTop: 13,
    backgroundColor: '#ffffff',
  },
  sectionContainer: {
    marginTop: 32,
    paddingHorizontal: 24,
  },
  sectionTitle: {
    fontSize: 24,
    fontWeight: '600',
  },
  sectionDescription: {
    marginTop: 8,
    fontSize: 18,
    fontWeight: '400',
  },
  highlight: {
    fontWeight: '700',
  },

  headerStyle: {
    fontSize: 14,
    color: '#ffffff',
    fontWeight: 'bold',
  },
  heading: {
    textAlign: 'center',
    fontSize: 18,
    color: 'blue',
    fontWeight: 'bold',
  },
});
