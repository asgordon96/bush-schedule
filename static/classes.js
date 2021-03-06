// Generated by CoffeeScript 1.3.3
(function() {

  $(function() {
    return $.get("/data", function(data, other) {
      var all_classes, classes_by_block, clear, fall, filter, show_classes, split_data, spring, winter;
      split_data = data.split("\t");
      fall = split_data[0].split('\n');
      winter = split_data[1].split('\n');
      spring = split_data[2].split('\n');
      classes_by_block = function(data) {
        var all_data, data_by_block, line, _i, _len;
        all_data = (function() {
          var _i, _len, _results;
          _results = [];
          for (_i = 0, _len = data.length; _i < _len; _i++) {
            line = data[_i];
            _results.push(line.split(","));
          }
          return _results;
        })();
        data_by_block = {
          A: [],
          B: [],
          C: [],
          D: [],
          E: [],
          F: []
        };
        for (_i = 0, _len = all_data.length; _i < _len; _i++) {
          line = all_data[_i];
          data_by_block[line[0]].push(line);
        }
        return data_by_block;
      };
      fall = classes_by_block(fall);
      winter = classes_by_block(winter);
      spring = classes_by_block(spring);
      all_classes = {
        'fall': fall,
        'winter': winter,
        'spring': spring
      };
      show_classes = function(classes) {
        var block, class_data, html_string, item, list, _i, _len, _ref, _results;
        _ref = Object.keys(classes);
        _results = [];
        for (_i = 0, _len = _ref.length; _i < _len; _i++) {
          block = _ref[_i];
          list = $("." + block);
          list.html("");
          _results.push((function() {
            var _j, _len1, _ref1, _results1;
            _ref1 = classes[block];
            _results1 = [];
            for (_j = 0, _len1 = _ref1.length; _j < _len1; _j++) {
              class_data = _ref1[_j];
              item = $("<li></li>").text("" + class_data[2]);
              item.addClass("class");
              item.data(class_data);
              html_string = "<h3>" + class_data[2] + "</h3><p>" + class_data[3] + "</p><p>Room: " + class_data[4] + "</p>";
              item.popover({
                content: html_string,
                html: true,
                placement: 'top',
                trigger: 'hover'
              });
              _results1.push(list.append(item));
            }
            return _results1;
          })());
        }
        return _results;
      };
      show_classes(fall);
      $("#term").change(function() {
        var term;
        term = $("#term").val();
        return show_classes(all_classes[term]);
      });
      filter = function(string, index) {
        var i, items, list_item, _i, _ref, _results;
        items = $("li.class");
        items.removeClass("selected");
        _results = [];
        for (i = _i = 0, _ref = items.length; 0 <= _ref ? _i < _ref : _i > _ref; i = 0 <= _ref ? ++_i : --_i) {
          list_item = $(items[i]);
          if (list_item.data()[index] === string) {
            _results.push(list_item.addClass("selected"));
          } else {
            _results.push(void 0);
          }
        }
        return _results;
      };
      $("select").change(function() {
        return filter($("#subject").val(), 1);
      });
      clear = function() {
        return $("li").removeClass("selected");
      };
      $("#clear").click(clear);
      $(document).on("click", "li.class", function(event) {
        return filter($(event.target).data()[2], 2);
      });
      $(document).on("dblclick", "li", function(event) {
        return $(event.target).toggleClass("choice");
      });
      $("select").chosen();
      return $("div.chosen-container").css("width", "125px");
    });
  });

}).call(this);
