#!/usr/bin/python
# -*- coding: utf-8 -*-
# all info about Paristech ecole and universities in China
# Created on 2008-11-19.
# $Id: paristech.py 26 2009-08-04 22:06:00Z guolin.mobi $
#

class Ecole(object):
    def __init__(self, acronym, name, website, desc=None):
        self.acronym = acronym
        self.name    = name
        self.website = website
        self.desc    = desc


class University(object):
    def __init__(self, acronym, name, name_en, website, desc=None):
        self.acronym = acronym
        self.name    = name
        self.name_en = name_en
        self.website = website
        self.desc    = desc


ECOLES = { "ENPC" :
           Ecole( acronym="ENPC",
                  name="Ecole Nationale des Ponts et Chaussées",
                  website="http://www.enpc.fr/" ),
           
           "ENST" :
           Ecole( acronym="ENST",
                  name="Ecole Nationale Supérieure des Télécommunications (aka. Télécom ParisTech)",
                  website="http://www.enst.fr/" ),
           
           "ENSAE" :
           Ecole( acronym="ENSAE",
                  name="Ecole Nationale de la Statistique et de l'Administration",
                  website="http://www.ensae.fr/" ),
           
           "ENSTA" :
           Ecole( acronym="ENSTA",
                  name="Ecole Nationale Supérieure de Techniques Avancées",
                  website="http://www.ensta.fr/" ),
           
           "ENSAM" :
           Ecole( acronym="ENSAM",
                  name="Ecole Nationale Supérieure d'Arts et Métiers",
                  website="http://www.ensam.fr/" ),
           
           "X" :
           Ecole( acronym="X",
                  name="Ecole Polytechnique",
                  website="http://www.polytechnique.fr/" ),
           
           "ENSCP" :
           Ecole( acronym="ENSCP",
                  name="Ecole Nationale Supérieure de Chimie de Paris",
                  website="http://www.enscp.fr/" ),
           
           "ESPCI" :
           Ecole( acronym="ESPCI",
                  name="Ecole Supérieure de Physique et de Chimie Industrielles de la Ville de Paris",
                  website="http://www.espci.fr/" ),
           
           "ENSMP" :
           Ecole( acronym="ENSMP",
                  name="Ecole Nationale Supérieure des Mines de Paris",
                  website="http://www.ensmp.fr/" ),
           
           "AgroParisTech" :
           Ecole( acronym="AgroParisTech",
                  name="AgroParisTech (INA P-G, ENGREF, ENSIA)",
                  website="http://www.agroparistech.fr/" ),
           
           "HEC" :
           Ecole( acronym="HEC",
                  name="Ecole des Hautes Etudes Commerciales",
                  website="http://www.hec.fr/" ),
				  

           # Add an ecole here:
           # "Acronym" :
           # Ecole( acronym="Acronym",
           #        name="Ecole Name",
           #        website="Ecole Website URL" ),
         
         } # ECOLES


UNIVERSITIES = { "PKU" :
                 University( acronym="PKU",
                             name="北京大学",
                             name_en="Peking University",
                             website="http://www.pku.edu.cn/" ),
                 
                 "Tsinghua" :
                 University( acronym="Tsinghua",
                             name="清华大学",
                             name_en="Tsinghua University",
                             website="http://www.tsinghua.edu.cn/" ),
                 
                 "CAU" :
                 University( acronym="CAU",
                             name="中国农业大学",
                             name_en="China Agricultural University",
                             website="http://www.cau.edu.cn/" ),
                 
                 "NJU" :
                 University( acronym="NJU",
                             name="南京大学",
                             name_en="Nanjing University",
                             website="http://www.nju.edu.cn/" ),
                 
                 "SEU" :
                 University( acronym="SEU",
                             name="东南大学",
                             name_en="Southeast University",
                             website="http://www.seu.edu.cn/" ),
                 
                 "NJAU" :
                 University( acronym="NJAU",
                             name="南京农业大学",
                             name_en="Nanjing Agricultural University",
                             website="http://www.njau.edu.cn/" ),
                 
                 "Tongji" :
                 University( acronym="Tongji",
                             name="同济大学",
                             name_en="Tongji University",
                             website="http://www.tongji.edu.cn/" ),
                 
                 "Fudan" :
                 University( acronym="Fudan",
                             name="复旦大学",
                             name_en="Fudan University",
                             website="http://www.fudan.edu.cn/" ),
                 
                 "SJTU" :
                 University( acronym="SJTU",
                             name="上海交通大学",
                             name_en="Shanghai Jiao Tong University",
                             website="http://www.sjtu.edu.cn/" ),
                 
                 "ZJU" :
                 University( acronym="ZJU",
                             name="浙江大学",
                             name_en="Zhe Jiang University",
                             website="http://www.zju.edu.cn/" ),
                 
                 # Add a Chinese university here:
                 # "Acronym" :
                 # University( acronym="Acronym",
                 #             name="University Name",
                 #             name_en="University Name in English",
                 #             website="University Website URL" ),
               
               } # UNIVERSITIES





