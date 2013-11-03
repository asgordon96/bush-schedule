$ ->
  $.get("/data", (data, other) -> 
    split_data = data.split("\t")
    fall = split_data[0].split('\n')
    winter = split_data[1].split('\n')
    spring = split_data[2].split('\n')
    
    classes_by_block = (data) ->
      all_data = (line.split(",") for line in data)
      data_by_block = { A:[], B:[], C:[], D:[], E:[], F:[] }
      for line in all_data
        data_by_block[line[0]].push(line)
      data_by_block
    
    fall = classes_by_block(fall)
    winter = classes_by_block(winter)
    spring = classes_by_block(spring)
    all_classes = { 'fall':fall, 'winter':winter, 'spring':spring  }
    
    show_classes = (classes) ->
      for block in Object.keys(classes)
        list = $(".#{block}")
        list.html("")
        for class_data in classes[block]
          item = $("<li></li>").text("#{class_data[2]}")
          item.addClass("class")
          item.data(class_data)
          html_string = "<h3>#{class_data[2]}</h3><p>#{class_data[3]}</p><p>Room: #{class_data[4]}</p>"
          item.popover({content:html_string, html:true, placement:'top', trigger:'hover'})
          list.append(item)
    
    show_classes(fall)
    
    $("#term").change( ->
      term = $("#term").val()
      show_classes(all_classes[term])
    )
    
    filter = (string, index) ->
      items = $("li.class")
      items.removeClass("selected")
      for i in [0...items.length]
        list_item = $(items[i])
        if list_item.data()[index] == string
          list_item.addClass("selected")
      
    $("#subject").change( -> filter($("#subject").val(), 1) )
    
    clear = ->
      $("li").removeClass("selected")
    
    $("#clear").click(clear)
    $(document).on("click", "li.class", (event) ->
      filter($(event.target).data()[2], 2)
    )
    
    $(document).on("dblclick", "li", (event) ->
      $(event.target).toggleClass("choice")
    )
    
    $("select").chosen()
    $("div.chosen-container").css("width", "125px")
    
    # code to hide the flash message
    hideFlash = -> $(".flash-messages").slideUp(500)
    window.setTimeout(hideFlash, 2500)
    
  )