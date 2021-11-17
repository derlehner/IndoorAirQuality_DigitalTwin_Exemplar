/*
 * JavaScript file for the application to demonstrate
 * using the API
 */

// Create the namespace instance
let ns = {};

// Create the model instance
ns.model = (function () {
  "use strict";

  let $event_pump = $("body");

  // Return the API
  return {
    read: function () {
      let ajax_options = {
        type: "GET",
        url: "api/sensordata",
        accepts: "application/json",
        dataType: "json",
      };
      $.ajax(ajax_options)
        .done(function (data) {
          $event_pump.trigger("model_read_success", [data]);
        })
        .fail(function (xhr, textStatus, errorThrown) {
          $event_pump.trigger("model_error", [xhr, textStatus, errorThrown]);
        });
    },
    create: function (id, container, instance, property, value) {
      let ajax_options = {
        type: "POST",
        url: "api/sensordata",
        accepts: "application/json",
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify({
          id: id,
          container: container,
          instance: instance,
          property: property,
          value: value,
        }),
      };
      $.ajax(ajax_options)
        .done(function (data) {
          $event_pump.trigger("model_create_success", [data]);
        })
        .fail(function (xhr, textStatus, errorThrown) {
          $event_pump.trigger("model_error", [xhr, textStatus, errorThrown]);
        });
    },
    update: function (id, container, instance, property, value) {
      let ajax_options = {
        type: "PUT",
        url: "api/sensordata/" + id,
        accepts: "application/json",
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify({
          id: id,
          container: container,
          instance: instance,
          property: property,
          value: value,
        }),
      };
      $.ajax(ajax_options)
        .done(function (data) {
          $event_pump.trigger("model_update_success", [data]);
        })
        .fail(function (xhr, textStatus, errorThrown) {
          $event_pump.trigger("model_error", [xhr, textStatus, errorThrown]);
        });
    },
    delete: function (id) {
      let ajax_options = {
        type: "DELETE",
        url: "api/sensordata/" + id,
        accepts: "application/json",
        contentType: "plain/text",
      };
      $.ajax(ajax_options)
        .done(function (data) {
          $event_pump.trigger("model_delete_success", [data]);
        })
        .fail(function (xhr, textStatus, errorThrown) {
          $event_pump.trigger("model_error", [xhr, textStatus, errorThrown]);
        });
    },
  };
})();

// Create the view instance
ns.view = (function () {
  "use strict";

  let $id = $("#id"),
    $container = $("#container"),
    $instance = $("#instance"),
    $property = $("#property"),
    $value = $("#value");

  // return the API
  return {
    reset: function () {
      $container.val(""),
        $instance.val(""),
        $property.val(""),
        $value.val(""),
        $id.val("").focus();
    },
    update_editor: function (id, container, instance, property, value) {
      $container.val(container);
      $instance.val(instance);
      $property.val(property);
      $value.val(value);
      $id.val(id).focus();
    },
    build_table: function (sensordata) {
      let rows = "";

      // clear the table
      $(".sensordata table > tbody").empty();

      // did we get a sensordata array?
      if (sensordata) {
        for (let i = 0, l = sensordata.length; i < l; i++) {
          rows += `<tr><td class="id">${sensordata[i].id}</td><td class="container">${sensordata[i].container}</td>
                              <td class="instance">${sensordata[i].instance}</td><td>${sensordata[i].time}</td>
                              <td class="property">${sensordata[i].property}</td><td class="value">${sensordata[i].value}</td>`;
        }
        $("table > tbody").append(rows);
      }
    },
    error: function (error_msg) {
      $(".error").text(error_msg).css("visibility", "visible");
      setTimeout(function () {
        $(".error").css("visibility", "hidden");
      }, 3000);
    },
  };
})();

// Create the controller
ns.controller = (function (m, v) {
  "use strict";

  let model = m,
    view = v,
    $event_pump = $("body"),
    $id = $("#id"),
    $container = $("#container"),
    $instance = $("#instance"),
    $property = $("#property"),
    $value = $("#value");

  // Get the data from the model after the controller is done initializing
  setTimeout(function () {
    model.read();
  }, 100);

  // Validate input
  function validate(id, container, instance, property) {
    return (
      id !== "" &&
      container !== "" &&
      instance !== "" &&
      property !== "" &&
      value !== ""
    );
  }

  // Create our event handlers
  $("#create").click(function (e) {
    let container = $container.val(),
      instance = $instance.val(),
      property = $property.val(),
      value = $value.val(),
      id = parseInt($id.val());

    e.preventDefault();

    if (validate(id, container, instance, property, value)) {
      model.create(id, container, instance, property, value);
    } else {
      alert("Problem with  input");
    }
  });

  $("#update").click(function (e) {
    let container = $container.val(),
      instance = $instance.val(),
      property = $property.val(),
      value = $value.val(),
      id = parseInt($id.val());

    e.preventDefault();

    if (validate(id, container, instance, property, value)) {
      model.update(id, container, instance, property, value);
    } else {
      alert("Problem with input");
    }
    e.preventDefault();
  });

  $("#delete").click(function (e) {
    let id = $id.val();

    e.preventDefault();

    if (validate("placeholder", id)) {
      model.delete(id);
    } else {
      alert("Problem with first or last name input");
    }
    e.preventDefault();
  });

  $("#reset").click(function () {
    view.reset();
  });

  $("table > tbody").on("dblclick", "tr", function (e) {
    let $target = $(e.target),
      id,
      container,
      instance,
      property,
      value;

    id = $target.parent().find("td.id").text();

    container = $target.parent().find("td.container").text();

    instance = $target.parent().find("td.instance").text();

    property = $target.parent().find("td.property").text();

    value = $target.parent().find("td.value").text();

    view.update_editor(id, container, instance, property, value);
  });

  // Handle the model events
  $event_pump.on("model_read_success", function (e, data) {
    view.build_table(data);
    view.reset();
  });

  $event_pump.on("model_create_success", function (e, data) {
    model.read();
  });

  $event_pump.on("model_update_success", function (e, data) {
    model.read();
  });

  $event_pump.on("model_delete_success", function (e, data) {
    model.read();
  });

  $event_pump.on("model_error", function (e, xhr, textStatus, errorThrown) {
    let error_msg =
      textStatus + ": " + errorThrown + " - " + xhr.responseJSON.detail;
    view.error(error_msg);
    console.log(error_msg);
  });
})(ns.model, ns.view);
