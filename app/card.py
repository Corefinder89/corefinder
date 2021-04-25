from textwrap import dedent


def card(json_obj, work_ex):
    phrase = "Soumyajit"
    topbar = "-" * len(phrase)
    bottombar = "-" * len(phrase)
    output = dedent(
        f"""
        {topbar}
        <{phrase}>
        {bottombar}
         \                   .,
           \         .      .TR   d'
             \      k,l    .R.b  .t .Je
               \   .P q.   a|.b .f .Z%              Name:               {json_obj.get("attributes").
                                                                            get("personal_details").get("name")}
                   .b .h  .E` # J: 2`     .
              .,.a .E  ,L.M'  ?:b `| ..J9!`.,       Designation:        {json_obj.get("attributes").get("profile").
                                                                            get("current_designation")}
               q,.h.M`   `..,   ..,""` ..2"`        Organization:       {json_obj.get("attributes").get("profile").
                                                                            get("organization")}
               .M, J8`   `:       `   3;            Working from:       {json_obj.get("attributes").get("profile").
                                                                            get("working_from")}
           .    Jk              ...,   `^7"90c.     Experience:         {work_ex}
            j,  ,!     .7"'`j,.|   .n.   ...        Ex-professional:    {json_obj.get("attributes").get("profile").
                                                                            get("ex_organization")}
           j, 7'     .r`     4:      L   `...
          ..,m.      J`    ..,|..    J`  7TWi       Linkedin:           {json_obj.get("attributes").get("profile").
                                                                            get("linkedin_profile")}
          ..JJ,.:    %    oo      ,. ....,          GitHub:             {json_obj.get("attributes").get("profile").
                                                                            get("github_profile")}
            .,E      3     7`g.M:    P  41          Bitbucket:          {json_obj.get("attributes").get("profile").
                                                                            get("bitbucket_profile")}
           JT7"'      O.   .J,;     ``  V"7N.       Highest degree:     {json_obj.get("attributes").get("education").
                                                                            get("highest_degree")}
           G.           ""Q+  .Zu.,!`      Z`       University:         {json_obj.get("attributes").get("education").
                                                                            get("university")}
           .9.. .         J&..J!       .  ,:
              7"9a                    JM"!
                 .5J.     ..        ..F`            Email:              {json_obj.get("attributes").
                                                                            get("personal_details").get("email")}
                    78a..   `    ..2'               Currently located:  {json_obj.get("attributes").
                                                                            get("personal_details").get("current_location")}
                        J9Ksaw0"'                   Zip code:           {json_obj.get("attributes").
                                                                            get("personal_details").get("zip_code")}
                       .EJ?A...a.
                       q...g...gi
                      .m...qa..,y:
                      .HQFNB&...mm
                       ,Z|,m.a.,dp
                    .,?f` ,E?:"^7b
                    `A| . .F^^7'^4,
                     .MMMMMMMMMMMQzna,
                 ...f"A.JdT     J:    Jp,
                  `JNa..........A....af`
                       `^^^^^'`
        """
    )

    return output
