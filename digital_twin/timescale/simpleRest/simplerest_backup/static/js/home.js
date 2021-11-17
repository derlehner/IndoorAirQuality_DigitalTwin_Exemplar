/*
 * JavaScript file for the application to demonstrate
 * using the API
 */

// Create the namespace instance
let ns = {};

// Create the model instance
ns.model = (function() {
    'use strict';

    let $event_pump = $('body');

    // Return the API
    return {
        'read': function() {
            let ajax_options = {
                type: 'GET',
                url: 'api/sensordata',
                data: {length: 100},
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_read_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        create: function(id,sensorname,roomnumber,co2,temperature,humidity) {
            let ajax_options = {
                type: 'POST',
                url: 'api/sensordata',
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    "id": id,
                    "sensorname": sensorname,
                    "roomnumber": roomnumber,
                    "co2": co2,
                    "temperature": temperature,
                    "humidity": humidity
                    })
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_create_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        update: function(id,sensorname,roomnumber,co2,temperature,humidity) {
            let ajax_options = {
                type: 'PUT',
                url: 'api/sensordata/' + id,
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    "id": id,
                    "sensorname": sensorname,
                    "roomnumber": roomnumber,
                    "co2": co2,
                    "temperature": temperature,
                    "humidity": humidity
                })
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_update_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        'delete': function(id) {
            let ajax_options = {
                type: 'DELETE',
                url: 'api/sensordata/' + id,
                accepts: 'application/json',
                contentType: 'plain/text'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_delete_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        }
    };
}());

// Create the view instance
ns.view = (function() {
    'use strict';

    let $id = $('#id'),
        $sensorname = $('#sensorname'),
        $roomnumber = $('#roomnumber'),
        $co2 = $('#co2'),
        $temperature = $('#temperature'),
        $humidity = $('#humidity');

    // return the API
    return {
        reset: function() {
            $sensorname.val(''),
            $roomnumber.val(''),
            $co2.val(''),
            $temperature.val(''),
            $humidity.val(''),
            $id.val('').focus();
        },
        update_editor: function(id,sensorname,roomnumber,co2,temperature,humidity) {
            $sensorname.val(sensorname);
            $roomnumber.val(roomnumber);
            $co2.val(co2);
            $temperature.val(temperature);
            $humidity.val(humidity);
            $id.val(id).focus();
        },
        build_table: function(sensordata) {
            let rows = ''

            // clear the table
            $('.sensordata table > tbody').empty();

            // did we get a sensordata array?
            if (sensordata) {
                for (let i=0, l=sensordata.length; i < l; i++) {
                    rows += `<tr><td class="id">${sensordata[i].id}</td><td class="sensorname">${sensordata[i].sensorname}</td>
                              <td class="roomnumber">${sensordata[i].roomnumber}</td><td>${sensordata[i].time}</td>
                              <td class="co2">${sensordata[i].co2}</td><td class="temperature">${sensordata[i].temperature}</td>
                              <td class="humidity">${sensordata[i].humidity}</td></tr>`;
                }
                $('table > tbody').append(rows);
            }
        },
        error: function(error_msg) {
            $('.error')
                .text(error_msg)
                .css('visibility', 'visible');
            setTimeout(function() {
                $('.error').css('visibility', 'hidden');
            }, 3000)
        }
    };
}());

// Create the controller
ns.controller = (function(m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body'),
        $id = $('#id'),
        $sensorname = $('#sensorname'),
        $roomnumber = $('#roomnumber'),
        $co2 = $('#co2'),
        $temperature = $('#temperature'),
        $humidity = $('#humidity');

    // Get the data from the model after the controller is done initializing
    setTimeout(function() {
        model.read();
    }, 100)

    // Validate input
    function validate(id, sensorname, roomnumber, co2, temperature, humidity) {
        return id !== "" && sensorname !== "" && roomnumber !== "" && co2 !== "" && temperature !== "" && humidity !== "";
    }

    // Create our event handlers
    $('#create').click(function(e) {
        let sensorname = $sensorname.val(),
            roomnumber = $roomnumber.val(),
            co2 = parseFloat($co2.val()),
            temperature = parseFloat($temperature.val()),
            humidity = parseFloat($humidity.val()),
            id = parseInt($id.val());

        e.preventDefault();

        if (validate(id,sensorname,roomnumber,co2,temperature,humidity)) {
            model.create(id,sensorname,roomnumber,co2,temperature,humidity)
        } else {
            alert('Problem with  input');
        }
    });

    $('#update').click(function(e) {
        let sensorname = $sensorname.val(),
            roomnumber = $roomnumber.val(),
            co2 = parseFloat($co2.val()),
            temperature = parseFloat($temperature.val()),
            humidity = parseFloat($humidity.val()),
            id = parseInt($id.val());

        e.preventDefault();

        if (validate(id,sensorname,roomnumber,co2,temperature,humidity)) {
            model.update(id,sensorname,roomnumber,co2,temperature,humidity)
        } else {
            alert('Problem with input');
        }
        e.preventDefault();
    });

    $('#delete').click(function(e) {
        let id = $id.val();

        e.preventDefault();

        if (validate('placeholder', id)) {
            model.delete(id)
        } else {
            alert('Problem with first or last name input');
        }
        e.preventDefault();
    });

    $('#reset').click(function() {
        view.reset();
    })

    $('table > tbody').on('dblclick', 'tr', function(e) {
        let $target = $(e.target),
                       id,
                       sensorname,
                       roomnumber,
                       co2,
                       temperature,
                       humidity;

        id = $target
            .parent()
            .find('td.id')
            .text();

        sensorname = $target
            .parent()
            .find('td.sensorname')
            .text();

        roomnumber = $target
            .parent()
            .find('td.roomnumber')
            .text();

        co2 = $target
            .parent()
            .find('td.co2')
            .text();

        temperature = $target
            .parent()
            .find('td.temperature')
            .text();

        humidity = $target
            .parent()
            .find('td.humidity')
            .text();

        view.update_editor(id,sensorname,roomnumber,co2,temperature,humidity);
    });

    // Handle the model events
    $event_pump.on('model_read_success', function(e, data) {
        view.build_table(data);
        view.reset();
    });

    $event_pump.on('model_create_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_update_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_delete_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_error', function(e, xhr, textStatus, errorThrown) {
        let error_msg = textStatus + ': ' + errorThrown + ' - ' + xhr.responseJSON.detail;
        view.error(error_msg);
        console.log(error_msg);
    })
}(ns.model, ns.view));