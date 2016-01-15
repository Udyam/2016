/**
 * Created by darknight on 15/1/16.
 */
var max_members = 5;
      var counter = 1;
      // TODO change as per event
      var events = {"" : 5,
                    "code42day" :"5",
                    "codedef" :"1",
                    "continnum" :"5",
                    "commnet" :"5",
                    "digisim" :"5",
                    "embedtron" :"5",
                    "funckit" :"5",
                    "ichip" :"5",
                    "ignite" :"5",
                    "krypto" :"5",
                    "mosaic" :"5",
                    "muse" :"5"
                    };

      $("#event_name").on("change", function(){
          max_members = parseInt(events[$('#event_name option:selected').val()]);
          if( $("#m" + (max_members+1) + "_field").length > 0){
              var i = max_members + 1;
              while(i <= 5){
                  $("#m"+(i)+"_field").remove();
                  i++;
              }
              counter = max_members;
          }
      });
    function add_member(){
        //dynamically adds a member to the team
        if(counter >= max_members){
            alert("Maximum "+max_members+" is/are allowed in "+$('#event_name option:selected').text()+" event");
        }
        else{
            counter++;
            var text =  '<fieldset id="m'+counter+'_field"> \
                            <legend style="text-align: center;">Member '+counter+' details:</legend>\
                            Name: <input type="text" name="member'+counter+'_name" required>&emsp;&emsp;\
                            Contact Number: <input type="text" name="member'+counter+'_contact" pattern="^[1-9][0-9]{9}$" required>&emsp;&emsp; \
                            Email: <input type="email" name="member'+counter+'_email" required>&emsp;&emsp;\
                            <a class="btn fa fa-remove fa-2x" \
                                onclick="remove_member(' + "'m"+counter+"_field'"+')"> \
                            </a>\
                        </fieldset>';
            $("#members_div").append(text);
        }
    }
    function remove_member(tag){
        $('#'+tag).remove();
        $mem_div = $("#members_div");
        $mem_div.children("fieldset").each(function(index) {
            var mem_id = index + 2;
            $(this).attr("id", "m" +mem_id+"_field");
            $child = $(this).children('input');
            $child.eq(0).attr("name", "member"+mem_id+"_name");
            $child.eq(1).attr("name", "member"+mem_id+"_contact");
            $child.eq(2).attr("name", "member"+mem_id+"_email");
            $(this).children("a").eq(0).attr("onclick","remove_member('m"+mem_id+"_field')");
            $(this).children("legend").eq(0).html("Member "+ mem_id + " details")
        });
        counter--;
    }

    function hide_menu(){
        $('#menu_list').attr("class", "hide");
    }

    function show_menu(){
        $('#menu_list').attr("class", "wow fadeInLeft");
    }
    $('#register_form').submit(function(){
      var registrationData = {
        'event': $('#event_name option:selected').val(),
        'team_name': $('input[name=team_name]').val(),
        'main_contact': {
            'name': $('input[name=member1_name]').val(),
            'contact': $('input[name=member1_contact]').val(),
            'email': $('input[name=member1_email]').val()
        },
        'team_details': []
      };
      var i = 1;
      while(i<=5) {
        registrationData.team_details.push({
          'name': $('input[name=member'+i+'_name]').val(),
          'contact': $('input[name=member'+i+'_contact]').val(),
          'email': $('input[name=member'+i+'_email]').val()
        });
        i++;
      }
      $.ajax({
        type: 'POST',
        url: '/',
          headers: { "X-CSRFToken": getCookie("csrftoken") },
          contentType: 'application/json; charset=utf-8',
        data: $.toJSON(registrationData),
        dataType: 'json'
      }).done(function(data) {
        console.log(data);
      });
    });
