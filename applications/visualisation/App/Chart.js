import React, {useState, useEffect} from 'react';
import {
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Button,
  Text,
  useColorScheme,
  FlatList,
  View,
} from 'react-native';
import {Header} from 'react-native-elements';
import {SafeAreaProvider} from 'react-native-safe-area-context';
import {
  VictoryBar,
  VictoryStack,
  VictoryGroup,
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

// https://49d10b83ed9e.ngrok.io
//rimport Ionicons from 'react-native-vector-icons/Ionicons';
function DetailsScreen() {
  return (
    <View style={{flex: 1, alignItems: 'center', justifyContent: 'center'}}>
      <Text>Details Screen</Text>
    </View>
  );
}
/* function App() {
  const [loading, setLoading] = useState(null);
  const [sensorData, setSensorData] = useState([]);
  const VictoryZoomVoronoiContainer = createContainer('zoom', 'voronoi');
  const [selectedDomain, setSelectedDomain] = useState();
  const [zoomDomain, setZoomDomain] = useState();
  const handleZoom = domain => {
    setSelectedDomain(domain);
  };
  const handleBrush = domain => {
    setZoomDomain(domain);
  };

  if (loading) return 'Loading...';
  return (
    <View style={styles.container}>
      <Header
        backgroundColor="#005fff"
        leftComponent={{icon: 'menu', color: '#fff'}}
        centerComponent={{
          text: 'Sensor Data',
          style: {color: '#fff', fontSize: 16, fontWeight: 'bold'},
          color: '#fff',
          fontSize: 14,
          fontWeight: 'bold',
        }}
        rightComponent={{
          icon: 'settings',
          color: '#fff',
        }}
      />

      <VictoryChart
        theme={VictoryTheme.material}
        width={400}
        height={400}
        padding={{top: 40, left: 70, right: 30, bottom: 100}}
        domainPadding={20}
        containerComponent={
          <VictoryZoomVoronoiContainer
            zoomDimension="x"
          
            zoomDomain={{x: [0, 5], y: [0, 8000]}}
            onZoomDomainChange={handleZoom}
           
          />
        }>
        <VictoryAxis fixLabelOverlap />
        <VictoryAxis dependentAxis />
        <VictoryAxis
          dependentAxis
          label="Count"
          style={{
            axisLabel: {padding: 50, fontSize: 15, fontWeight: 'bold'},
            axis: {stroke: 'black'},
            ticks: {stroke: 'purple', size: 5},
          }}
        />
        <VictoryAxis
          independentAxis
          label="Hourly Interval"
          style={{
            axisLabel: {padding: 30, fontSize: 15, fontWeight: 'bold'},
            axis: {stroke: 'black'},
            ticks: {stroke: 'purple', size: 5},
          }}
        />

        <VictoryGroup offset={20} colorScale={'qualitative'}>
          <VictoryBar
            data={[
              {x: 1, y: 1},
              {x: 2, y: 2},
              {x: 3, y: 5},
            ]}
          />
          <VictoryBar
            data={[
              {x: 1, y: 2},
              {x: 2, y: 1},
              {x: 3, y: 7},
            ]}
          />
          <VictoryBar
            data={[
              {x: 1, y: 3},
              {x: 2, y: 4},
              {x: 3, y: 9},
            ]}
          />
        </VictoryGroup>
      </VictoryChart>
    </View>
  );
} */

const styles = StyleSheet.create({
  container: {
    flex: 1,

    paddingTop: 13,
    backgroundColor: '#eeeeee',
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
});

export default DetailsScreen;
