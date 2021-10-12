import 'react-native-gesture-handler';
import * as React from 'react';
import {Pressable, Button, View, Text, StyleSheet} from 'react-native';
import {Header, Card} from 'react-native-elements';
import {NavigationContainer} from '@react-navigation/native';
import {createStackNavigator} from '@react-navigation/stack';
import overview from './OverviewCo2';
import chartRoom101 from './Room101';
import chartRoom102 from './Room102';
import chartRoom103 from './Room103';

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator
        initialRouteName="Overview of Co2 levels in Building "
        headerMode="screen"
        screenOptions={{
          headerTintColor: 'white',
          headerStyle: {backgroundColor: '#2C76F0'},
          headerTitleStyle: {fontSize: 22, alignItems: 'center'},
        }}>
        <Stack.Screen
          name="Overview of Co2 levels in Building "
          component={overview}
        />
        <Stack.Screen name="Co2 in Room101" component={chartRoom101} />
        <Stack.Screen name="Co2 in Room102" component={chartRoom102} />
        <Stack.Screen name="Co2 in Room103" component={chartRoom103} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    backgroundColor: '#eeeeee',
  },

  Heading: {
    fontWeight: 'bold',
    color: '#0087ff',
    fontSize: 16,
  },
  cardRow: {
    //flex: 1,
    flexDirection: 'row',
  },
  modelCard: {
    borderRadius: 20,
    borderColor: 'lightgrey',
    paddingBottom: 10,
  },
  cardStyle1: {
    borderRadius: 20,
    width: 180,
    marginRight: 0,
    marginLeft: 10,
    borderColor: 'lightgrey',
    backgroundColor: 'orange',
  },
  cardStyle2: {
    borderRadius: 20,
    width: 180,
    marginRight: 0,
    marginLeft: 10,
    borderColor: 'lightgrey',
    backgroundColor: '#FF6F5A',
  },
  cardStyle3: {
    borderRadius: 20,
    width: 180,
    marginRight: 0,
    marginLeft: 10,
    borderColor: 'lightgrey',
    backgroundColor: '#FDDE66',
  },
  cardStyle4: {
    borderRadius: 20,
    width: 180,
    marginRight: 0,
    marginLeft: 10,
    borderColor: 'lightgrey',
    backgroundColor: '#83EE68',
  },
  cardTitle: {
    color: '#ffffff',
    fontSize: 15,
  },
  subHeading: {
    fontWeight: 'bold',
  },
  image: {
    width: 150,
    height: 70,
  },
});
