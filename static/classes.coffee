$ ->
  $.get("/data", (data, other) -> 
    split_data = data.split("\t")
    fall = split_data[0].split('\n')
    winter = split_data[1].split('\n')
    spring = split_data[2].split('\n')

    fall_data = (line.split(",") for line in fall)
    data_by_block = { A:[], B:[], C:[], D:[], E:[], F:[] }
    for line in fall_data
      data_by_block[line[0]].push(line)
    
    for block in Object.keys(data_by_block)
      list = $(".#{block}")
      for class_data in data_by_block[block]
        item = $("<li></li>").text("#{class_data[2]}")
        item.data(class_data)
        html_string = "<h3>#{class_data[2]}</h3><p>#{class_data[3]}</p><p>Room: #{class_data[4]}</p>"
        item.popover({content:html_string, html:true, placement:'top', trigger:'hover'})
        list.append(item)
      
    filter = (string, index) ->
      items = $("li")
      items.removeClass("selected")
      for i in [0...items.length]
        list_item = $(items[i])
        if list_item.data()[index] == string
          list_item.addClass("selected")
      
    $("select").change( -> filter($("select").val(), 1) )
    
    clear = ->
      $("li").removeClass("selected")
    
    $("#clear").click(clear)
    $("li").click( (event) ->
      filter($(event.target).data()[2], 2)
    )
    
    $("li").dblclick( (event) ->
      $(event.target).toggleClass("choice")
    )
    
    $("select").chosen()
  )