import React from 'react';
import {TouchableOpacity, StyleSheet, Text, View} from 'react-native';
import {Card} from 'react-native-elements';

function overview({navigation}) {
  return (
    <View style={styles.container}>
      <View style={styles.cardRow}>
        <TouchableOpacity
          onPress={() => {
            navigation.navigate('Sensor Data');
          }}>
          <Card containerStyle={styles.cardStyle1}>
            <Text>
              <Text style={styles.subHeading}>Lobby: 100 - Raspberry 1</Text>
            </Text>
            <Text>
              <Text style={styles.subHeading}></Text>
            </Text>
            <Card.Image
              style={styles.image}
              source={require('./images/Room.jpg')}
            />

            <Text style={styles.subHeading}>Co2 level: 689.60</Text>

            <Text style={styles.subHeading}>Risk: Low</Text>
          </Card>
        </TouchableOpacity>
        <Card containerStyle={styles.cardStyle2}>
          <Text>
            <Text style={styles.subHeading}>Room: 101 - Raspberry 2</Text>
          </Text>
          <Text>
            <Text style={styles.subHeading}></Text>
          </Text>
          <Card.Image
            style={styles.image}
            source={require('./images/Room.jpg')}
          />

          <Text style={styles.subHeading}>Co2 level: 2500.50</Text>

          <Text style={styles.subHeading}>Risk: High</Text>
        </Card>
        <Card containerStyle={styles.cardStyle3}>
          <Text>
            <Text style={styles.subHeading}>Room: 102 - Raspberry 3</Text>
          </Text>
          <Text>
            <Text style={styles.subHeading}></Text>
          </Text>
          <Card.Image
            style={styles.image}
            source={require('./images/Room.jpg')}
          />

          <Text style={styles.subHeading}>Co2 level: 1000.90</Text>

          <Text style={styles.subHeading}>Risk: Medium</Text>
        </Card>
      </View>
    </View>
  );
}

export default overview;
const styles = StyleSheet.create({
  container: {
    flex: 1,

    backgroundColor: '#eeeeee',
  },

  Heading: {
    fontWeight: 'bold',
    color: '#0087ff',
    fontSize: 14,
  },
  cardRow: {
    flexDirection: 'column',
  },
  modelCard: {
    borderRadius: 20,
    borderColor: 'lightgrey',
    paddingBottom: 10,
  },
  cardStyle1: {
    borderRadius: 20,
    width: 350,
    height: 220,
    marginRight: 0,
    marginLeft: 10,
    borderColor: 'lightgrey',
    backgroundColor: '#83EE68',
    padding: 10,
  },
  cardStyle2: {
    borderRadius: 20,
    width: 350,
    height: 220,
    marginRight: 0,
    marginLeft: 10,
    borderColor: 'lightgrey',
    backgroundColor: '#FF6F5A',
  },
  cardStyle3: {
    borderRadius: 20,
    width: 350,
    height: 220,
    marginRight: 0,
    marginLeft: 10,
    borderColor: 'lightgrey',
    backgroundColor: 'orange',
  },
  cardStyle4: {
    borderRadius: 20,
    width: 180,
    height: 220,
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
    fontSize: 18,
    padding: 2,
  },
  image: {
    padding: 10,
    width: 350,
    height: 100,
  },
});
