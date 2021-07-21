import React, {useState, useEffect} from 'react';
import {
  Pressable,
  SafeAreaView,
  ScrollView,
  StyleSheet,
  Text,
  View,
} from 'react-native';
import {Card} from 'react-native-elements';
import {Header} from 'react-native-elements';
function overview({navigation}) {
  //function HomeScreen({navigation}) {
  return (
    <View style={styles.container}>
      {/*   <Header
          backgroundColor="#005fff"
          leftComponent={{icon: 'menu', color: '#fff'}}
          centerComponent={{
            text: 'Feature Overview',
            style: {color: '#fff', fontSize: 16, fontWeight: 'bold'},
            color: '#fff',
            fontSize: 14,
            textColor: '#fff',
            fontWeight: 'bold',
          }}
          rightComponent={{
            icon: 'settings',
            color: '#fff',
          }}
        /> */}

      <Pressable
        onPress={() => {
          navigation.navigate('Details');
          // setTimesPressed((current) => current + 1);
        }}>
        <View style={styles.cardRow}>
          <Card containerStyle={styles.cardStyle1}>
            {/*   <Card.Title style={styles.cardTitle}>Scp-3 </Card.Title> */}
            <Text>
              <Text style={styles.subHeading}>Room:</Text> 0080
            </Text>
            <Card.Image
              style={styles.image}
              source={require('./images/Room.jpg')}
            />
            <Text>
              <Text style={styles.subHeading}>Co2 level:</Text> 2500.50
            </Text>
            <Text>
              <Text style={styles.subHeading}>Risk:</Text> High
            </Text>
          </Card>
          <Card containerStyle={styles.cardStyle2}>
            {/*  <Card.Title style={styles.cardTitle}>Scp-3 </Card.Title> */}

            <Text>
              <Text style={styles.subHeading}>Room:</Text> 0086
            </Text>
            <Card.Image
              style={styles.image}
              source={require('./images/Room.jpg')}
            />
            <Text>
              <Text style={styles.subHeading}>Co2 level:</Text> 3600.90
            </Text>
            <Text>
              <Text style={styles.subHeading}>Risk:</Text> Very High
            </Text>
          </Card>
        </View>
      </Pressable>
      <Pressable
        onPress={() => {
          navigation.navigate('Details');
        }}>
        <View style={styles.cardRow}>
          <Card containerStyle={styles.cardStyle3}>
            {/*  <Card.Title style={styles.cardTitle}>Scp-3</Card.Title> */}
            <Text>
              <Text style={styles.subHeading}>Room:</Text> 0090
            </Text>
            <Card.Image
              style={styles.image}
              source={require('./images/Room.jpg')}
            />
            <Text>
              <Text style={styles.subHeading}>Co2 level:</Text> 1250.80
            </Text>
            <Text>
              <Text style={styles.subHeading}>Risk:</Text> Medium
            </Text>
          </Card>
          <Card containerStyle={styles.cardStyle4}>
            {/*  <Card.Title style={styles.cardTitle}>Scp-3</Card.Title> */}
            <Text>
              <Text style={styles.subHeading}>Room:</Text> 0076
            </Text>
            <Card.Image
              style={styles.image}
              source={require('./images/Room.jpg')}
            />
            <Text>
              <Text style={styles.subHeading}>Co2 level:</Text> 1000.25
            </Text>
            <Text>
              <Text style={styles.subHeading}>Risk:</Text> Low
            </Text>
          </Card>
        </View>
      </Pressable>
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
