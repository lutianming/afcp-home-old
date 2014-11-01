#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2008 ZHENG Zhong <heavyzheng nospam-at gmail D0T com>
# - http://heavyz.blogspot.com/
# - http://buggarden.blogspot.com/
#
# Created on 2008-12-08.
# $Id: resources.py 26 2009-08-04 22:06:00Z guolin.mobi $
#

class BannerImage(object):
    def __init__(self, id, url, title, desc):
        self.id    = id
        self.url   = url
        self.title = title
        self.desc  = desc


BANNER_IMAGES = ( BannerImage( id="Forum_Horizon_Chine_2010_1",
                               url="/forum/",
                               title="Forum Horizon Chine,",
                               desc="Taken by AFCP on 2010-05-20" ),
                  BannerImage( id="Forum_Horizon_Chine_2010_2",
                               url="/forum/",
                               title="Forum Horizon Chine,",
                               desc="Taken by AFCP on 2010-05-20" ),
                  BannerImage( id="Forum_Horizon_Chine_2010_3",
                               url="/forum/",
                               title="Forum Horizon Chine,",
                               desc="Taken by AFCP on 2010-05-20" ), 
                  BannerImage( id="Forum_Horizon_Chine_2010_4",
                               url="/forum/",
                               title="Forum Horizon Chine,",
                               desc="Taken by AFCP on 2010-05-20" ),
                  BannerImage( id="Forum_Horizon_Chine_2010_5",
                               url="/forum/",
                               title="Forum Horizon Chine,",
                               desc="Taken by AFCP on 2010-05-20" ), 
                  BannerImage( id="Forum_Horizon_Chine_2010_6",
                               url="/forum/",
                               title="Forum Horizon Chine,",
                               desc="Taken by AFCP on 2010-05-20" ),
                  BannerImage( id="Forum_Horizon_Chine_2010_7",
                               url="/forum/",
                               title="Forum Horizon Chine,",
                               desc="Taken by AFCP on 2010-05-20" ), 
                  BannerImage( id="Forum_Horizon_Chine_2010_8",
                               url="/forum/",
                               title="Forum Horizon Chine,",
                               desc="Taken by AFCP on 2010-05-20" ),
                  BannerImage( id="Forum_Horizon_Chine_2010_9",
                               url="/forum/",
                               title="Forum Horizon Chine,",
                               desc="Taken by AFCP on 2010-05-20" ), 
                  BannerImage( id="Forum_Horizon_Chine_2010_10",
                               url="/forum/",
                               title="Forum Horizon Chine,",
                               desc="Taken by AFCP on 2010-05-20" ),
                 
                  BannerImage( id="Forum_Horizon_Chine_2011_11",
                               url="/forum/",
                               title="Forum Horizon Chine,",
                               desc="Taken by AFCP on 2011-05-12" ),
                  BannerImage( id="Forum_Horizon_Chine_2011_12",
                               url="/forum/",
                               title="Forum Horizon Chine,",
                               desc="Taken by AFCP on 2011-05-12" ),
                  BannerImage( id="Forum_Horizon_Chine_2011_13",
                               url="/forum/",
                               title="Forum Horizon Chine,",
                               desc="Taken by AFCP on 2011-05-12" ),
                  BannerImage( id="Forum_Horizon_Chine_2011_14",
                               url="/forum/",
                               title="Forum Horizon Chine,",
                               desc="Taken by AFCP on 2011-05-12" ),
                  BannerImage( id="Forum_Horizon_Chine_2011_15",
                               url="/forum/",
                               title="Forum Horizon Chine,",
                               desc="Taken by AFCP on 2011-05-12" ),
                  BannerImage( id="Forum_Horizon_Chine_2011_16",
                               url="/forum/",
                               title="Forum Horizon Chine,",
                               desc="Taken by AFCP on 2011-05-12" ),
                  # Add a banner image here:
                  # BannerImage( id="id (static image file base name)",
                  #              url="external url",
                  #              title="image title",
                  #              desc="description" ),
                ) # BANNER_IMAGES

# Liste des adresses e-mail des contacts des entreprises à qui les candidatures sont envoyées.
# L'id correspond à l'id indiquée dans les formulaires de postulation
# Exemple :
#company_emails = {
#                  '1': "architruc <archi.truc@yahoo.fr>, aol emd <antoine.ory-lamballe@mines-paristech.fr>"
#                  }
company_emails = {
                  '1': "hong.wang@edf.fr, christian.keim@edf.fr", # EDF - Urban planning engineer - R&D
                  '2': "hong.wang@edf.fr, jose-carlos.valle-marcos@edf.fr", # EDF - Carbon capture processes engineer - R&D
                  '3': "hong.wang@edf.fr, francois-xavier.testard-vaillant@edf.fr", # EDF - Open Innovation research engineer - R&D
                  '4': "hong.wang@edf.fr, xavier.yang@edf.fr", # EDF - Electric power grid engineer with experience - EDF Beijing R&D
                  '5': "hong.wang@edf.fr, xavier.yang@edf.fr", # EDF - Electric power grid engineer - EDF Beijing R&D
                  '6': "rm.ap-sghr@total.com", # Total - Assistant Manager - Aviation (SUPPLY & MARKETING – ASIA PACIFIC)
                  '7': "rm.ap-sghr@total.com",  # Total - HSE Manager (REFINING & MARKETING – ASIA-PACIFIC)
                  '8': "recrutement.bnpparibas.com", # BNP - Analyste Développeur IT H/F (BNP Paribas Securities Services)
                  '9': "recrutement.bnpparibas.com", # BNP - Analyste Développeur Projet d’Innovation 2SlovesIT H/F (BNP Paribas Securities Services)
                  '10': "recrutement.bnpparibas.com", # BNP - Assistant Coordination de Projets IT H/F (BNP Paribas Securities Services)
                  '11': "stagesbnpp-ip@bnpparibas.com", # BNP - Assistant Recherche Quantitative H/F (pôle Investment Solutions- Investment Partners)
                  '12': "recrutement.bnpparibas.com", # BNP - Gestionnaire IT support transverse H/F
                  '13': "edfbaphr@edf.fr", # EDF - Open Innovation Research Engineer
                  }
application_cc = u'AFCP <AFCParisTech@gmail.com>, Antoine ORY-LAMBALLE <antoine.ory-lamballe@mines-paristech.fr>, ZHENG Ban <ban.zheng.x2005@gmail.com>'

contactus_emails = u'AFCP <AFCParisTech@gmail.com>, ban.zheng.x2005@gmail.com, luoyudenis@gmail.com'
