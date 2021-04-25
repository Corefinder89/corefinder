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
               \   .P q.   a|.b .f .Z%
                   .b .h  .E` # J: 2`     .         Name:               {json_obj.get("attributes").
                                                                            get("personal_details").get("name")}
              .,.a .E  ,L.M'  ?:b `| ..J9!`.,       Aka:                {json_obj.get("attributes").
                                                                            get("personal_details").get("also_known_as")}
               q,.h.M`   `..,   ..,""` ..2"`
               .M, J8`   `:       `   3;            Designation:        {json_obj.get("attributes").get("profile").
                                                                            get("current_designation")}
           .    Jk              ...,   `^7"90c.     Organization:       {json_obj.get("attributes").get("profile").
                                                                            get("organization")}
            j,  ,!     .7"'`j,.|   .n.   ...        Working from:       {json_obj.get("attributes").get("profile").
                                                                            get("working_from")}
           j, 7'     .r`     4:      L   `...       Experience:         {work_ex}
          ..,m.      J`    ..,|..    J`  7TWi       Ex-professional:    {json_obj.get("attributes").get("profile").
                                                                            get("ex_organization")}
          ..JJ,.:    %    oo      ,. ....,
            .,E      3     7`g.M:    P  41          Linkedin:           {json_obj.get("attributes").get("profile").
                                                                            get("linkedin_profile")}
           JT7"'      O.   .J,;     ``  V"7N.       GitHub:             {json_obj.get("attributes").get("profile").
                                                                            get("github_profile")}
           G.           ""Q+  .Zu.,!`      Z`       Bitbucket:          {json_obj.get("attributes").get("profile").
                                                                            get("bitbucket_profile")}
           .9.. .         J&..J!       .  ,:        Highest degree:     {json_obj.get("attributes").get("education").
                                                                            get("highest_degree")}
              7"9a                    JM"!          University:         {json_obj.get("attributes").get("education").
                                                                            get("university")}
                 .5J.     ..        ..F`
                    78a..   `    ..2'               Email:              {json_obj.get("attributes").
                                                                            get("personal_details").get("email")}
                        J9Ksaw0"'                   Currently located:  {json_obj.get("attributes").
                                                                            get("personal_details").get("current_location")}
                       .EJ?A...a.                   Zip code:           {json_obj.get("attributes").
                                                                            get("personal_details").get("zip_code")}
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
